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
api = tweepy.API(auth)

filename = input("enter file name: ")

with open(filename,'w', newline='') as f:
    w = csv.writer(f)

    f = open(filename,'w', newline='')
    w.writerow(["Tweet ID", "Username", "User ID", "Hashtags", "Mentions", "Text"])
    search = tweepy.Cursor(api.home_timeline, include_entitities=True).items(10)

    for tweet in search:
        tweetid = tweet.id
        username = tweet.user.screen_name
        userid = tweet.user.id
        hashtags = []
        hashtagsArray = tweet.entities.get('hashtags')
        for ht in hashtagsArray:
            hashtags.append(ht['text'])
        mentions = {}
        mentionsArray = tweet.entities.get('user_mentions')
        for um in mentionsArray:
            mentions[um['id_str']] = um['screen_name']
#        OLD CODE BELOW:
#        mentionsName = []
#        mentionsId = []
#        mentionsArray = tweet.entities.get('user_mentions')
#        if 'user_mentions' in tweet.entities:
#            count = 0
#            for eachDict in mentionsArray:
#                mentionsDict = mentionsArray[count]
#                count += 1
#                for key in mentionsDict:
#                    if key == 'screen_name':
#                        mentionsName.append(mentionsDict.get(key))
#                    elif key == 'id_str':
#                        mentionsId.append(mentionsDict.get(key))
#                    else:
#                        mentionsName == None
#                        mentionsId == None
        tweettext = tweet.text.encode("UTF-8")
        tweet = [tweetid, username, userid, hashtags, mentions, tweettext]

        w.writerow(tweet)

    f.close()

print("All done!")
