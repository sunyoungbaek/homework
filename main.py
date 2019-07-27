import sys
from word_probs import wordProbs

if __name__== "__main__":
  wordProbs.getUniBigramWeights(sys.argv[1])  
