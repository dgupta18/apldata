#reddit to csv

import praw
import csv
import io

reddit = praw.Reddit(client_id='ex70CcTSYUjhFg',
                     client_secret='Bahi7zIZ0eEsxMjcBIVdlk-9DQI',
                     user_agent='testscript by /u/dgtest16',
                     username='dgtest16')

filenum = str(input('enter output file number: '))
filename = "rdCSVsubreddit" + filenum + ".csv"
print("filename is: " + filename)

with open(filename, 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',')

    f = open(filename,'w', newline='')
    writer.writerow([
        'subredditID',
        'submissionTitle',
        'submissionID',
        'commentCreated',
        'commentID',
        'commentText',
        'authorName',
        'authorID',
    ])

    search = str(input('enter search term: '))
    subreddit = reddit.subreddit(search)
    submissions = subreddit.submissions()
    for submission in submissions:
        # subID = submission.id
        # subTitle = submission.title
        comments = submission.comments
        count = 0
        for comment in comments:
            if comment is not None:
                # commentText = comment.body.encode("UTF-8")
                # authorName = comment.author
                authorID = ""
                try:
                    authorID = comment.author.id
                except:
                    authorID = 'none'
                info = [
                    subreddit.id,
                    submission.title.encode("UTF-8"),
                    submission.id,
                    comment.created,
                    comment.id,
                    comment.body.encode("UTF-8"),
                    comment.author,
                    authorID
                ]
                writer.writerow(info)

                count += 1
                if count >= 2:
                    break

f.close()
print("Done")
