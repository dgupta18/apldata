#reddit to xml

import praw
import csv
import io

reddit = praw.Reddit(client_id='ex70CcTSYUjhFg',
                     client_secret='Bahi7zIZ0eEsxMjcBIVdlk-9DQI',
                     user_agent='testscript by /u/dgtest16',
                     username='dgtest16')

filenum = str(input('enter output file number: '))
filename = "rdCSVsubreddit" + filenum + ".csv"
print(filename)

with open(filename, 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',')

    f = open(filename,'w', newline='')
    writer.writerow([
        'subredditID',
        'submissionID',
        'submissionTitle',
        'commentCreated',
        'commentID',
        'commentText',
        'authorName',
        # 'authorID',
    ])

    search = 'JHU'
    subreddit = reddit.subreddit(search, limit=1)
    submissions = subreddit.submissions()
    for submission in submissions:
        subID = submission.id
        subTitle = submission.title
        comments = submission.comments
        for comment in comments:
            if comment is not None:
                commentCreated = comment.created
                commentID = comment.id
                commentText = comment.body.encode("UTF-8")
                # io.open(commentBody)
                authorName = comment.author
                # authorID = authorName.id
                info = [subreddit.id, subID, subTitle, commentID, commentCreated, commentText, authorName]
                writer.writerow(info)

f.close()
print("Done")
