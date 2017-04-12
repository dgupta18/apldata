#reddit to xml

import praw

reddit = praw.Reddit(client_id='ex70CcTSYUjhFg',
                     client_secret='Bahi7zIZ0eEsxMjcBIVdlk-9DQI',
                     user_agent='testscript by /u/dgtest16',
                     username='dgtest16')

subreddit = reddit.subreddit('office')
print(reddit.user.me())

# hello
