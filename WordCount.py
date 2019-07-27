import pandas as pd
from urllib.request import urlopen
from collections import defaultdict
from collections import OrderedDict
import numpy as np

class WordCounts:
    def __init__(self, unigramUrl, bigramUrl):
        self.unigramUrl = unigramUrl
        self.bigramUrl = bigramUrl

        # initialize unigram variables
        self.unigramCounts = defaultdict(lambda : 0)
        self.totalUnigrams = 0
        self.numUnigramKeys = 0
        self._initializeUnigramCounts()
        
        # initialize bigram variables
        self.bigramCounts = defaultdict(lambda : defaultdict(lambda: 0))
        self.totalBigrams = 0
        self.numBigramKeys = 0
        self._initializeBigramCounts()
            
    def _initializeUnigramCounts(self):
        data = urlopen(self.unigramUrl)
        nk, tot = 0, 0
        for line in data:
            word, count = line.split()
            self.unigramCounts[word] = int(count)
            nk += 1
            tot += int(count)
        self.numUnigramKeys = nk
        self.totalUnigrams = tot
        
    def _initializeBigramCounts(self):
        data = urlopen(self.bigramUrl)
        nk, tot = 0, 0
        for line in data:
            word1, word2, count = line.split()
            self.bigramCounts[word1][word2] = int(count)
            nk += 1
            tot += int(count)
        self.numBigramKeys = nk
        self.totalBigrams = tot
    
    def getUnigramCount(self, word):
        return self.unigramCounts[word]
    
    def getTotalUnigramCount(self):
        return self.totalUnigrams
    
    def getUniqueUnigramCount(self):
        return self.numUnigramKeys
    
    def addUnigram(self, word):
        # if unigram is never seen before, add to unique unigram
        if self.unigramCounts[word] == 0:
            self.numUnigramKeys += 1
        self.unigramCounts[word] = self.unigramCounts[word] + 1    
        self.totalUnigrams += 1
    
    def getBigramCount(self, word1, word2):
        return self.bigramCounts[word1][word2]
    
    def getTotalBigramCount(self):
        return self.totalBigrams
    
    def getUniqueBigramCount(self):
        return self.numBigramKeys
    
    def getUniqueBigramCountAfterGivenWord(self, word):
        return len(self.bigramCounts[word].keys())
    
    def addBigram(self, word1, word2):
        if self.bigramCounts[word1][word2] == 0:
            self.numBigramCounts += 1
        self.bigramCounts[word1][word2] = self.bigramCounts[word1][word2] + 1  
        self.totalBigrams += 1

        
# Define unigram and bigram corpus URL
unigramUrl = 'https://norvig.com/ngrams/count_1w.txt'
bigramUrl = 'https://norvig.com/ngrams/count_2w.txt'

# Create a WordCounts object based on the URLs
wordCounts = WordCounts(unigramUrl, bigramUrl)

