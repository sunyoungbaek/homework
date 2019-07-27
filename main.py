import sys
from .WordCount import wordCounts
from .WordProbs import wordProbs

if __name__== "__main__":
  wordProbs.getUniBigramWeights(sys.argv[1])  
