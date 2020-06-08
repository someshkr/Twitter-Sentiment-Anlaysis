# -*- coding: utf-8 -*-
"""
Created on Mon May  4 17:41:07 2020

@author: SOMESH
"""

import twitter
import json
import re
#Keys, secret keys and access tokens management.

#Consumer API keys
CONSUMER_KEY = "HIdden"
CONSUMER_SECRET = "Hidden"

#Access token & access token secret

OAUTH_TOKEN = "Hidden"
OAUTH_TOKEN_SECRET = "HIdden"


# Creating the authentication object
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

# Creating the API object while passing in auth information
api = twitter.Twitter(auth=auth)

print(api)

INDIA_WOE_ID = 23424848
india_trends = api.trends.place(_id = INDIA_WOE_ID)

trendInd = {}

#for trending in india_trends[0]['trends']:
#    print(trending['name'], '-----' , trending['tweet_volume'])

q = 'Nepal'
count = 100

search_results = api.search.tweets(q=q, count=count)

statuses = search_results['statuses']



for _ in range(5):
    print("Length of statuses", len(statuses))
    try:
        next_results = search_results['search_metadata']['next_results']
    except: # No more results when next_results doesn't exist
        break
        
    # Create a dictionary from next_results, which has the following form:
    # ?max_id=313519052523986943&q=NCAA&include_entities=1
    kwargs = dict([ kv.split('=') for kv in next_results[1:].split("&") ])
    
    search_results = api.search.tweets(**kwargs)
    statuses += search_results['statuses']

content = []
users = []
liked = []
liked_count = []
retweet = []
rt_count = []
source = []
created = []
place = []
tid = []
tag_name = []
#for regular expression 
pattern = re.compile(r'<[^>]+>')


for i in range(100):
    content.append(statuses[i]['text'])
    users.append(statuses[i]['user']['name'])
    liked.append(statuses[i]['favorited'])
    liked_count.append(statuses[i]['favorite_count'])
    retweet.append(statuses[i]['retweeted'])
    rt_count.append(statuses[i]['retweet_count'])                               
    source.append(pattern.sub('',statuses[i]['source']))
    created.append(statuses[i]['user']['created_at'])
    place.append(statuses[i]['coordinates'])
    tid.append(statuses[i]['id_str'])
    tag_name.append(statuses[i]['user']['screen_name'])
    
import pandas as pd

data = pd.DataFrame({'users':users,
                     'tagid':tag_name,
                     'tid':tid,
                     'content':content, 
                     'date':created,
                     'liked':liked,
                     'liked-count':liked_count,
                     'retweet':retweet,
                     'retweet_count':rt_count,
                     'place':place,
                     'source':source
                     })




































































   

