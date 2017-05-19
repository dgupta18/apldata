# tumblr data using yaml format
from tumblpy import Tumblpy
import yaml

consumer_key = "nYCRA3c4qFYvAy1j4YXlcEquEcT6w8yGVouAv9uNMlgumpV7AO"
consumer_secret = "aJqWc3abjqXltB4YYvBukLTQnc6eUACGk6TtNh7s4QM6hWG5Ia"
oauth_token = "zOXRlhngtkS59nTb1FWNrOXcOkzDlURYR0FKAdYFajoMHgqMzW"
oauth_token_secret = "PPyimZwbq4t8r69is1EubtkU5EivAvAIxKIcfaCFIF6c4Yhnmd"

t = Tumblpy(
    consumer_key,
    consumer_secret,
    oauth_token,
    oauth_token_secret
)

all_info = t.post("user/info")
blog = all_info["user"]["blogs"][0]

query = str(input("enter tag to search: "))
num = 0
data = {}
postArray = []

while True:
    posts = t.get("tagged", params={"offset":num, "tag":query})
    numPosts = len(posts)

    for post in posts:
        postDict = {}
        postDict["blog_name"] = post["blog_name"]
        postDict["post_id"] = post["id"]
        postDict["timestamp"] = post["timestamp"]
        postDict["tags"] = post["tags"]
        postDict["note_count"] = post["note_count"]

        if "trail" not in post: continue
        trailArray = []
        trail = post["trail"]
        for reblog in trail:
            if reblog["is_current_item"] == reblog["is_root_item"]: continue
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

data["posts"] = postArray

filenum = str(input('enter output file number: '))
filename = "tumblrYAMLtagged" + filenum + ".yaml"
with open(filename, "w") as outfile:
    yaml.dump(data, outfile, default_flow_style=False)

print('Done')
