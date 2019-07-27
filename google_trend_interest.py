import sys
from pytrends.request import TrendReq

def googleTrendInterest(query):
    words = query.lower().split()
    
    pytrend = TrendReq(hl='en-US', geo='US')
    pytrend.build_payload([words[0], words[1], query], cat=0, timeframe='today 5-y')
    result = pytrend.interest_over_time()
    result = result.iloc[:, :3].sum()   
    
    
if __name__== "__main__":
    query = sys.argv[1]
    
    # If query is not a bigram, return message
    if len(words) != 2:
        return 'this word is not a bigram'
    
    df = googleTrendInterest(query)
    sys.stdout.write(str(dict(result)))
