facebook_posts = [
    {"likes": 34, "comments": 4},
    {"likes": 49, "comments": 4},
    {"shares": 12, "comments": 4},
    {"likes": 30, "comments": 4},
    {"likes": 3, "comments": 4}
]
likes = 0
for post in facebook_posts:
    try:
        likes = likes + post["likes"]
    except:
        likes = likes + 0

print("You got a total of " + str(likes) + " likes")