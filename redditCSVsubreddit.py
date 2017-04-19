#reddit to xml

import praw
import csv

reddit = praw.Reddit(client_id='ex70CcTSYUjhFg',
                     client_secret='Bahi7zIZ0eEsxMjcBIVdlk-9DQI',
                     user_agent='testscript by /u/dgtest16',
                     username='dgtest16')

# search = 'DunderMifflin'
search = 'JHUAPL'   # hoping to create a merge conflict here
subreddit = reddit.subreddit(search)
submissions = subreddit.submissions()
for submission in submissions:
    subID = submission.id
    subTitle = submission.title
    print(submission, subID, subTitle)

#filenum = str(input('enter output file number: '))
#filename = "redditCSVsubreddit" + filenum + ".csv"

#with open(filename, 'w') as csvfile:
#    writer = csv.writer(csvfile, delimiter=',')
#    writer.writerow(['forum_id', 'submission_id', 'comment_id', 'user'])
#    submissions = subreddit.submissions()
#    for submission in submissions:
#        if submission is not None:
#            for comment in submission.comments:
#                if comment is not None:
#                    info = [subreddit.id, submission.id, comment.id, comment.author.id, comment.author]
#                    writer.writerow(info)
#
#print("All done!")
