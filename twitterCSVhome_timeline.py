# trying to print results from twitter API call into a csv file

import tweepy
from tweepy import OAuthHandler
import csv

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

filenum = str(input('enter output file number: '))
filename = "twCSVhome" + filenum + ".csv"
print(filename)

with open(filename,'w', newline='') as f:
    w = csv.writer(f)

    f = open(filename,'w', newline='')
    w.writerow([
        "Tweet ID",
        "Tweet Created",
        "Username",
        "User ID",
        "User Location",
        "Hashtags",
        "Mentions",
        "Text"
    ])
    search = tweepy.Cursor(api.home_timeline, include_entitities=True).items(180)

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

        tweet = [
            tweet.id,
            tweet.created_at,
            tweet.user.screen_name,
            tweet.user.id,
            userLocation,
            hashtags,
            mentions,
            tweet.text.encode("UTF-8")
        ]
        w.writerow(tweet)

    f.close()

print("Done")
