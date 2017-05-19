#reddit to xml

import praw
import xml.etree.ElementTree as et
from xml.etree.ElementTree import ElementTree, Element, SubElement, tostring

reddit = praw.Reddit(client_id='ex70CcTSYUjhFg',
                     client_secret='Bahi7zIZ0eEsxMjcBIVdlk-9DQI',
                     user_agent='testscript by /u/dgtest16',
                     username='dgtest16')

search = str(input("enter search term: "))
subredditSearch = reddit.subreddit(search)
submissions = subredditSearch.submissions()

data = Element('data')
subreddit = SubElement(data, 'subreddit')
subreddit.text = str(subredditSearch.id)

count = 0
for sub in submissions:
    if sub is None: continue
    submission = SubElement(subreddit, 'submission')
    submission.text = str(sub.id)

    comments = SubElement(submission, 'comments')
    for com in sub.comments:
        if com is None: continue
        comment = SubElement(comments, 'comment')

        commentCreated = SubElement(comment, 'commentCreated')
        commentCreated.text = ""
        try:
            commentCreated.text = str(com.created)
        except:
            commentCreated.text = "none"

        if com.id is not None:
            commentID = SubElement(comment, 'commentID')
            commentID.text = str(com.id)

        if com.body is not None:
            commentText = SubElement(comment, 'commentText')
            commentText.text = str(com.body)

        if com.author is not None:
            authorName = SubElement(comment, 'authorName')
            authorName.text = str(com.author.name)

        authorID = SubElement(comment, 'authorID')
        authorID.text = ""
        try:
            authorID.text = str(com.author.id)
        except:
            authorID.text = "none"

    count += 1
    if count >= 100:
        break

filenum = str(input('enter output file number: '))
filename = "redditXMLsubreddit" + filenum + ".xml"
with open(filename, 'wb') as outfile:
    tree = et.ElementTree(data)
    tree.write(outfile)
