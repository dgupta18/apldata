# tumblr data using yaml format
from tumblpy import Tumblpy
import yaml

t = Tumblpy(
    "nYCRA3c4qFYvAy1j4YXlcEquEcT6w8yGVouAv9uNMlgumpV7AO",
    "aJqWc3abjqXltB4YYvBukLTQnc6eUACGk6TtNh7s4QM6hWG5Ia",
    "zOXRlhngtkS59nTb1FWNrOXcOkzDlURYR0FKAdYFajoMHgqMzW",
    "PPyimZwbq4t8r69is1EubtkU5EivAvAIxKIcfaCFIF6c4Yhnmd"
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

        post_id = post["id"]
        timestamp = post["timestamp"]
        tags = post["tags"]
        note_count = post["note_count"]

        postDict["post_id"] = post_id
        postDict["timestamp"] = timestamp
        postDict["tags"] = tags
        postDict["note_count"] = note_count

        if "trail" not in post: continue
        trailArray = []
        trail = post["trail"]
        for reblog in trail:
            trailDict = {}

            reblog_name = str(reblog["blog"]["name"])
            reblog_post_id = str(reblog["post"]["id"])
            reblog_content_raw = str(reblog["content_raw"])

            trailDict["reblog_name"] = reblog_name
            trailDict["reblog_post_id"] = reblog_post_id
            trailDict["reblog_content_raw"] = reblog_content_raw

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
