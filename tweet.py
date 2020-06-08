# -*- coding: utf-8 -*-
"""
Created on Mon May  4 18:43:06 2020

@author: SOMESH
"""
import tweepy
import json
import re
from access_twitter_keys import Access
from Preprocessing import Prep_text
#from Sentiment_Subjective import Sent_sub

a = Access()
#authentication object creation
auth = tweepy.OAuthHandler(a.CONSUMER_KEY, a.CONSUMER_SECRET)
auth.set_access_token(a.ACCESS_TOKEN, a.ACCESS_TOKEN_SECRET)


# Creating the API object while passing in auth information
api = tweepy.API(auth)
print(api)
#23424848
trends = api.trends_place(23424848)[0]['trends']
print('trending item    ----------  Tweet_vol')
for i in range(10):
    print(trends[i]['name'],'---------',trends[i]['tweet_volume'])
    
    
q = '#935Days'


search_results = tweepy.Cursor(api.search,q=q,tweet_mode = 'extended',
                               wait_on_rate_limit = True, wait_on_rate_limit_notify = True, 
                               include_entities=True).items(100)

status = []
fullname = []
screenname = []
source= []
date_time = []
retweet = []
retweet_count = []
liked =[]
liked_count= []
language = []
tid = []
place = []

for tweet in search_results:
    try:
        status.append(tweet.retweeted_status.full_text)
    except AttributeError:  # Not a Retweet
        status.append(tweet.full_text)
    source.append(tweet.source)
    date_time.append(tweet.created_at)
    liked.append(tweet.favorited)
    liked_count.append(tweet.favorite_count)
    language.append(tweet.lang) 
    tid.append(tweet.id)
    retweet.append(tweet.retweeted)
    retweet_count.append(tweet.retweet_count)         
    fullname.append(tweet.user.name)
    screenname.append(tweet.user.screen_name)
 
    
    
from pymongo import MongoClient    
client = MongoClient('mongodb://localhost:27017/')

mydb = client['Twitter']

mycol = mydb['hashtags']



datadict = { 'users':fullname,
            'tagid':screenname,
            'id':tid,
            'content':status,
            'language':language,
            'date':date_time,
            'liked':liked,
            'liked-count':liked_count,
            'retweet':retweet,
            'retweet_count':retweet_count,
            'source':source,
                     }

x = mycol.insert_one(datadict)
print(x.inserted_id)
import pandas as pd

data = pd.DataFrame(datadict)

#data.to_csv(r'F:\DATA\twiiter.csv')

data  = data[data['language'] == 'en']
'''
def Preprocessing_text(text):
    lemmatizer = WordNetLemmatizer()
    text = text.lower()
    text = re.sub('\W+',' ', text)
    text = nltk.word_tokenize(text)    
    text = [lemmatizer.lemmatize(word) for word in text if word not in set(stopwords.words('english'))]   
    return text
'''

b = Prep_text()
round1 = lambda x: Preprocessing_text(x)
data_clean = pd.DataFrame(data.content.apply(b.round1))


from textblob import TextBlob
            
pol = lambda x: TextBlob(x).sentiment.polarity
sub = lambda x: TextBlob(x).sentiment.subjectivity

sentimentCreation(data,'polarity',pol)
subjectiveCreation(data,'subjectivity',sub)
    
    
