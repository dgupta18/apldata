# trying to print results from twitter API call into a csv file

import tweepy
from tweepy import OAuthHandler
import csv

consumer_key = 'DeOD1wjPQBNUjov9Fu40yO1l3'
consumer_secret = 'kjI7TaTBNxibTTJk0EV0QbgO9myYniaEEqH6R6BkxokzmPSn02'
access_token = '726966067-xzNYN7xTXWB0Sw7Zwgb719fXNyEH4v5hXUpyszJj'
access_secret = 'z2QOPZEhC8VIiVIjXNvjRu4rjmpGEGzaNhRpjnOcVXeJ3'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

filenum = str(input('enter output file number: '))
filename = "twCSVhome" + filenum + ".csv"
print(filename)

with open(filename,'w', newline='') as f:
    w = csv.writer(f)

    f = open(filename,'w', newline='')
    w.writerow(["Tweet ID", "Tweet Created", "Username", "User ID", "User Location", "Hashtags", "Mentions", "Text"])
    search = tweepy.Cursor(api.home_timeline, include_entitities=True).items(180)

    for tweet in search:
        tweetID = tweet.id
        createdAt = tweet.created_at
        username = tweet.user.screen_name
        userID = tweet.user.id
        userLocation = tweet.user.location if tweet.user.location is not None else "null"
        hashtags = []
        hashtagsArray = tweet.entities.get('hashtags')
        for ht in hashtagsArray:
            hashtags.append(ht['text'])
        mentions = {}
        mentionsArray = tweet.entities.get('user_mentions')
        for um in mentionsArray:s
            mentions[um['id_str']] = um['screen_name']
        tweetText = tweet.text.encode("UTF-8")

        tweet = [tweetID, createdAt, username, userID, userLocation, hashtags, mentions, tweetText]
        w.writerow(tweet)

    f.close()

print("Done")
