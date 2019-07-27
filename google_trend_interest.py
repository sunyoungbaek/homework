import sys
from pytrends.request import TrendReq

def googleTrendInterest(words):
    pytrend = TrendReq(hl='en-US', geo='US')
    pytrend.build_payload([words[0], words[1], words[0] + ' ' + words[1]], cat=0, timeframe='today 5-y')
    result = pytrend.interest_over_time()
    result = result.iloc[:, :3].sum()   
    
    
if __name__== "__main__":
    query = sys.argv[1]
    words = query.lower().split()
    
    # If query is not a bigram, return message
    if len(words) != 2:
        sys.stdout.write('this word is not a bigram')
    else:
        df = googleTrendInterest(words)
        sys.stdout.write(str(dict(df)))
