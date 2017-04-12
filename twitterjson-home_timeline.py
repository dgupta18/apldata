# twitter home timeline, output as JSON

import tweepy
from tweepy import OAuthHandler
import json
import pprint

pp = pprint.PrettyPrinter(indent=2)

consumer_key = 'DeOD1wjPQBNUjov9Fu40yO1l3'
consumer_secret = 'kjI7TaTBNxibTTJk0EV0QbgO9myYniaEEqH6R6BkxokzmPSn02'
access_token = '726966067-xzNYN7xTXWB0Sw7Zwgb719fXNyEH4v5hXUpyszJj'
access_secret = 'z2QOPZEhC8VIiVIjXNvjRu4rjmpGEGzaNhRpjnOcVXeJ3'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

filenum = str(input('enter output file number: '))
filename = "twitterJSONhome" + filenum + ".json"
print(filename)

search = tweepy.Cursor(api.home_timeline, include_entitities=True).items(10)

tweetData = []

for tweet in search:
    hashtags = []
    hashtagsArray = tweet.entities.get('hashtags')
    for ht in hashtagsArray:
        hashtags.append(ht['text'])
    mentions = {}
    mentionsArray = tweet.entities.get('user_mentions')
    for um in mentionsArray:
        mentions[um['id_str']] = um['screen_name']
#    tweettext = tweet.text.encode("UTF-8")
    twt = {
        'TweetID':tweet.id_str,
        'Username':tweet.user.screen_name,
        'UserID':tweet.user.id_str,
        'Hashtags':hashtags,
        'MentionedUsers':mentions,
        'Text':tweet.text
    }
    tweetData.append(twt)

pp.pprint(tweetData)

with open(filename, 'w') as outfile:
    json.dump(tweetData, outfile)

print('All done!')
