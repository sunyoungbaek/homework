class WordProbs:
    def __init__(self, wordCount):
        self.wordCount = wordCount
    
    def getUnigramProb(self, word):
        uc = self.wordCount.getUnigramCount(word)
        tc = self.wordCount.getTotalUnigramCount()
        
        return (uc + 1) / (tc + 10)
    
    def getBigramGivenUnigramProb(self, word1, word2):
        bc = self.wordCount.getBigramCount(word1, word2)
        uc1 = self.wordCount.getUnigramCount(word1) 
        ubc1 = self.wordCount.getUniqueBigramCountAfterGivenWord(word1)
        
        return (max(bc - d, 0) / uc1) + (d / uc1) * ubc1 * self.getUnigramProb(word1)
        
    def getRelativeStrengthScore(self, word1, word2):
        return np.log(self.getBigramGivenUnigramProb(self, word1, word2)) - np.log(self.getUnigramProb(word2))
    
    def getUniBigramWeights(query):
        words = query.split()
        weights = {}
        for word in words:
            weights[word] = -np.log(getUnigramProb(word))
        
        for i, word2 in enumerate(words[1:]):
            word1 = words[i]
            weights[word1 + ' ' + word2] = getRelativeStrengthScore(word1, word2)
        
        for i, word in enumerate(words):
            words[i-1] + ' ' + word
            word + ' ' + words[i+1]
