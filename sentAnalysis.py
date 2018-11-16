from textblob import TextBlob
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
import tweepy
import csv

'''
wiki = TextBlob("hai is very angry on himself")
print(wiki.tags)
print(wiki.words)
print(wiki.sentiment.polarity)
'''

def writeInCsv(tweet, sentiment):
   with open('sentAnalysis.csv', 'a', newline='', encoding="utf-8") as f:
       thewriter = csv.writer(f)
       #thewriter.writerow(['TWEET','SENTIMENT'])
       thewriter.writerow([tweet, sentiment])


consumer_key= 'loUjIpC4y05DV552XTbHRadwh'
consumer_secret= 'e25VVl7DVomRTHWJq6sdivtU84Mlneb9nXr2sv017qzuh1j7u1'

accessToken = '4609963946-27FVQ2rkXRyqpRvI6GjCpaE0bGOlCx0gP2sh1nY'
accessTokenSecret = 'qaZyffA9Mxpq4mA9Opypygw1sfYxsOpacnkq102bwaGy5'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

tweets = api.search('Trump')

for tweet in tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    #print(analysis.sentiment)
    if analysis.sentiment.polarity > 0.0:
        sentiment = 'positive'
    elif analysis.sentiment.polarity == 0.0:
        sentiment = 'neutral'
    else:
        sentiment = 'negative'
    writeInCsv(tweet.text, sentiment)





