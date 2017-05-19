# twitter home timeline, output as JSON

import tweepy
from tweepy import OAuthHandler
import json

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

search = tweepy.Cursor(api.home_timeline, include_entitities=True).items(180)

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
        'UserLocation':userLocation,
        'Hashtags':hashtags,
        'MentionedUsers':mentions,
        'Text':str(tweet.text.encode("UTF-8"))
    }
    tweetData.append(twt)

filenum = str(input('enter output file number: '))
filename = "twJSONhome" + filenum + ".json"
print(filename)
with open(filename, 'w') as outfile:
    json.dump(tweetData, outfile)

print('Done')
