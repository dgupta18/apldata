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
query = "jhu"

num = 0
data = {}
postArray = []

while True:
    posts = t.get("tagged", params={"offset":num, "tag":query})
    numPosts = len(posts)

    for post in posts:
        postDict = {}

        blog_name = post["blog_name"]
        post_id = post["id"]
        timestamp = post["timestamp"]
        tags = post["tags"]
        note_count = post["note_count"]

        postDict["blog_name"] = blog_name
        postDict["post_id"] = post_id
        postDict["timestamp"] = timestamp
        postDict["tags"] = tags
        postDict["note_count"] = note_count

        if "trail" not in post: continue
        trailArray = []
        trail = post["trail"]
        for reblog in trail:
            trailDict = {}
            if reblog["is_current_item"] == reblog["is_root_item"]: continue
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

data["posts"] = postArray

filenum = str(input('enter output file number: '))
filename = "tumblrYAMLtagged" + filenum + ".yaml"
with open(filename, "w") as outfile:
    yaml.dump(data, outfile, default_flow_style=False)

print('Done')
