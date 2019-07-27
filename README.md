# Homework

## Commands
python main.py "mountain view startup"
python google_trend_interest.py "ipad walmart"

## Sample Result from Main.py
'mountain view startp':
{'mountain view': 0.4899983193661052, 'startup': 0.3333333333333333, 'mountain': 0.08833417365028073, 'view startup': 0.0, 'view': 0.08833417365028073}

'ipad walmart':
{'ipad walmart': 0.0, 'ipad': 0.5, 'walmart': 0.5}

'ice cream social in san francisco':
{'ice cream': 0.3333333333333333, 'social in': 0.0, 'san francisco': 0.3333333333333333, 'san': 0.0, 'francisco': 0.0, 'social': 0.16666666666666666, 'in san': 0.0, 'in': 0.16666666666666666, 'ice': 0.0, 'cream social': 0.0, 'cream': 0.0}

'beauty and the beast':
{'beauty and': 0.07082758985981812, 'the beast': 0.34969838165787204, 'the': 0.026321459438805428, 'beast': 0.07515080917106398, 'beauty': 0.21458620507009094, 'and the': 0.0976586994645171, 'and': 0.16575685533783238}

'the fastest animal in the world':
{'the fastest': 0.3333333320697086, 'animal in': 0.0, 'the world': 0.0002792506540196216, 'the': 4.476094505927714e-09, 'world': 0.16652704133965684, 'animal': 0.16666666666666663, 'in the': 0.3330540749907493, 'in': 0.00013962917129199207, 'fastest animal': 0.0, 'fastest': 6.318123246806805e-10}

'how to learn a foreign language'
{'how to': 0.33333127904757676, 'learn a': 0.0, 'foreign language': 0.006939595346527511, 'foreign': 0.0, 'language': 0.16319686899340288, 'learn': 0.16666563953342817, 'a foreign': 0.32639373798680577, 'a': 0.0034697976732637557, 'how': 1.0271428782515633e-06, 'to learn': 2.054266476946977e-06, 'to': 9.639778074978371e-12}

## What's to be improved
Small weights (<0.1) are generally meaningless. They should be muted and re-normalized.

In 'beauty and the beast', 'beauty' (0.21) and (0.16) the beast (0.35) are the main scorers. 'and' is just conjunction and could have been lower weighted. 

In ''the fastest animal in the world', 'the fastest' (0.33) 'animal' (0.17), 'in the' (0.33), 'world' (0.16) are the main scorers. Instead of 'in the' + 'world', it would make more sense as 'in' + 'the world' grammatically. 

In 'how to learn a foreign language', 'how to' (0.33) 'learn' (0.17) 'a foreign' (0.33) 'language' (0.16) are the main scorers. Here, 'a foreign' doesn't really make sense, and it shoube 'a' + 'foreign language' instead. But since 'a' is so often used whenever 'foreign' modifier is used, this model doesn't know how to separate them (even though P(w2|w1) must be small, this model doesn't seem to penalize 'a''s frequency enough).

In all cases, we can see that 'in', 'and', 'the' are overweighted or over-joined (detected as bigram). Exploring how to weaken their importance using f(-log(uni/bigram prob)) can be helpful. Probabilities functions are already provided in WordProbs class.

## Attempt to use Google Trend
I used pytrends package.
(Make sure to pip install git+https://github.com/GeneralMills/pytrends. Version 4.6 has a major bug)

Explored using top_charts() and trending_searches(), but most of them are people's names or trendy terms (movie, show, game names, etc), so they were not useful.

I provided a file to look at unigram/bigram interests in Google Trend, given bigram query. This helps understanding strength of unigrams/bigrams. 








