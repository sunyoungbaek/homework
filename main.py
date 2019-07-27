import sys
from word_probs import wordProbs

if __name__== "__main__":
  weights = wordProbs.getUniBigramWeights(sys.argv[1])
  sys.stdout.write(weights)
