# twitter search for hashtag, output as JSON

import tweepy
from tweepy import OAuthHandler
import json

consumer_key = 'DeOD1wjPQBNUjov9Fu40yO1l3'
consumer_secret = 'kjI7TaTBNxibTTJk0EV0QbgO9myYniaEEqH6R6BkxokzmPSn02'
access_token = '726966067-xzNYN7xTXWB0Sw7Zwgb719fXNyEH4v5hXUpyszJj'
access_secret = 'z2QOPZEhC8VIiVIjXNvjRu4rjmpGEGzaNhRpjnOcVXeJ3'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

query = str(input("enter search term: "))
search = tweepy.Cursor(api.search,q=query).items(100)

tweetData = []

for tweet in search:
    userLocation = ""
    try:
        userLocation = tweet.user.location
    except:
        userLocation = "none"
    hashtags = []
    hashtagsArray = tweet.entities.get('hashtags')
    for ht in hashtagsArray:
        hashtags.append(ht['text'])
    mentions = {}
    mentionsArray = tweet.entities.get('user_mentions')
    for um in mentionsArray:
        mentions[um['id_str']] = um['screen_name']
    twt = {
        'TweetID':tweet.id_str,
        'CreatedAt':str(tweet.created_at),
        'Username':str(tweet.user.screen_name),
        'UserID':tweet.user.id_str,
        'UserLocation':str(userLocation),
        'Hashtags':hashtags,
        'MentionedUsers':mentions,
        'Text':str(tweet.text.encode("UTF-8"))
    }
    tweetData.append(twt)

filenum = str(input('enter output file number: '))
filename = "twJSONsearch" + filenum + ".json"
print(filename)
with open(filename, 'w') as outfile:
    json.dump(tweetData, outfile)

print('Done')
