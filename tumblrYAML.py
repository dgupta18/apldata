# tumblr data using yaml format
from tumblpy import Tumblpy
import yaml

consumer_key = ""
consumer_secret = ""
oauth_token = ""
oauth_token_secret = ""

t = Tumblpy(
    consumer_key,
    consumer_secret,
    oauth_token,
    oauth_token_secret
)

all_info = t.post("user/info")
blog = all_info["user"]["blogs"][0]
blog_name = str(blog["name"])
blog_url = str(blog["url"])

num = 0
blogDict = {}
postArray = []
blogDict["blog_name"] = blog_name
blogDict["blog_url"] = blog_url

while True:
    postsAll = t.get("posts", blog_url=blog_url, params={"offset":num})
    posts = postsAll["posts"]
    numPosts = len(posts)

    for post in posts:
        postDict = {}
        postDict["post_id"] = post["id"]
        postDict["timestamp"] = post["timestamp"]
        postDict["tags"] = post["tags"]
        postDict["note_count"] = post["note_count"]

        if "trail" not in post: continue
        trailArray = []
        trail = post["trail"]
        for reblog in trail:
            trailDict = {}
            trailDict["reblog_name"] = str(reblog["blog"]["name"])
            trailDict["reblog_post_id"] = str(reblog["post"]["id"])
            trailDict["reblog_content_raw"] = str(reblog["content_raw"])
            trailArray.append(trailDict)
        postDict["trail"] = trailArray
        postArray.append(postDict)

    num = num + numPosts
    if numPosts < 20 or num >= 1000:
        break

blogDict["posts"] = postArray

filenum = str(input('enter output file number: '))
filename = "tumblrYAML" + filenum + ".yaml"
with open(filename, "w") as outfile:
    yaml.dump(blogDict, outfile, default_flow_style=False)

print('Done')
