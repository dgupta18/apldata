#reddit to xml

import praw
import collections
import xml.etree.ElementTree as et
from xml.etree.ElementTree import ElementTree, Element, SubElement, tostring
import xml.dom.minidom as dom

reddit = praw.Reddit(client_id='ex70CcTSYUjhFg',
                     client_secret='Bahi7zIZ0eEsxMjcBIVdlk-9DQI',
                     user_agent='testscript by /u/dgtest16',
                     username='dgtest16')

search = 'JHU'
subredditSearch = reddit.subreddit(search)
submissions = subredditSearch.submissions()

data = Element('data')
subreddit = SubElement(data, 'subreddit')
subreddit.text = subredditSearch.id

for sub in submissions:
    if sub is None: continue
    submission = SubElement(subreddit, 'submission')
    submission.text = sub.id
    comments = SubElement(submission, 'comments')
    for com in sub.comments:
        if com is None: continue
        comment = SubElement(comments, 'comment')

        commentCreated = SubElement(comment, 'commentCreated')
        commentCreated.text = com.created
        if com.id is not None:
            commentID = SubElement(comment, 'commentID')
            commentID.text = com.id

        if com.body is not None:
            commentText = SubElement(comment, 'commentText')
            commentText.text = com.body

        if com.author is not None:
            authorName = SubElement(comment, 'authorName')
            authorName.text = com.author.name if com.author.name is not None else "NA"

            # authorID = SubElement(comment, 'authorID')
            # authorID.text = com.author.id if com.author.id is not None else "NA"

filenum = str(input('enter output file number: '))
filename = "redditXMLsubreddit" + filenum + ".xml"
with open(filename, 'w') as outfile:
    tree = et.ElementTree(str(data))
    tree.write(outfile)

print('Done')
