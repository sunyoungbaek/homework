import pandas as pd
from urllib.request import urlopen
from collections import defaultdict
from collections import OrderedDict
import numpy as np

class WordProbs:
    # static variable - % of unknown unique words based on the corpus
    unknownWordProb = 0.05
    
    def __init__(self, wordCount):
        self.wordCount = wordCount
    
    def _getUnigramProb(self, word):
        uc = self.wordCount.getUnigramCount(word)
        tc = self.wordCount.getTotalUnigramCount()
        # Total vocabulary size: V = N(unique words in corpus) + N(unique unseen words).
        # N(unique unseen words) is interpolated from seen vocab size.
        V = self.wordCount.getUniqueUnigramCount() * 1 / (1 - self.unknownWordProb)
        # Laplace smooth by assuming 1 missing observation of all vocabulary          
        return (uc + 1) / (tc + V)  
    
    def _getBigramGivenUnigramProb(self, word1, word2):
        bc = self.wordCount.getBigramCount(word1, word2)
        uc1 = self.wordCount.getUnigramCount(word1) 
        ubc1 = self.wordCount.getUniqueBigramCountAfterGivenWord(word1)
        # add 1 to all unigram counts for smoothing
        smoothingFactor = ubc1 / (ubc1 + uc1 + 1)
        
        return (1 - smoothingFactor) * bc / (uc1 + 1) + smoothingFactor * self._getUnigramProb(word2)

    def _getBigramProb(self, word1, word2):
        return self._getUnigramProb(word1) * self._getBigramGivenUnigramProb(word1, word2)      
        
    def _getRelativeStrengthScore(self, word1, word2):
        return max(self._getBigramGivenUnigramProb(word1, word2) / self._getUnigramProb(word2), 1.0)
    
    def _addDictionaries(self, dict_A, dict_B, a, b):
        dict_full = defaultdict(lambda : 0)
        for k, v in dict_A.items():
            dict_full[k] = dict_full[k] + v * a
        for k, v in dict_B.items():
            dict_full[k] = dict_full[k] + v * b
        return dict_full 
    
    def _createBigram(self, word_A, word_B):
        return (word_A.decode() + ' ' + word_B.decode()).encode()
    
    def _probabilityOfFormingBigram(self, w1, w2):
        # Cap odds at 100 to not have NaN error 
        x = min(self._getRelativeStrengthScore(w1, w2) - 1.0, 100)
        return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

    def _scoreWeights(self, words):
        memory = [{}] * len(words)
        memory[len(words) - 1] = {words[len(words) - 1]: 1.0}
        for i in range(len(words) - 1, 0, -1):
            p = self._probabilityOfFormingBigram(words[i-1], words[i])
            bigram = self._createBigram(words[i-1], words[i])
            
            # Each word can form a bigram with the next word with probability p,
            # or be a standlone unigram with probability (1-p)
            if i == len(words) - 1:
                case1 = {bigram: 2.0}
                case2 = self._addDictionaries({words[i-1]: 1.0}, memory[i], 1, 1)                                
            else:
                case1 = self._addDictionaries({bigram: 2.0}, memory[i+1], 1, 1)
                case2 = self._addDictionaries({words[i-1]: 1.0}, memory[i], 1, 1)
            memory[i-1] = self._addDictionaries(case1, case2, p, 1-p)
                
        return memory[0]
    
    def _normalizeWeights(self, weights):
        decodedWeights = {}
        totalVal = sum(list(weights.values()))
        for k, v in weights.items():
            decodedWeights[k.decode()] = v / totalVal
        return decodedWeights   
    
    def getUniBigramWeights(self, query):
        words = query.lower().encode().split()
        if len(words) == 0:
            return {}
        
        weights = dict(self._scoreWeights(words))
        normalizedWeights = self._normalizeWeights(weights)
        return normalizedWeights           
