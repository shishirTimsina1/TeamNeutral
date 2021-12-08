# exec(open('loadScript.py').read())

import json
from blog.models import Post

#use posts.json or posts2.json
with open('posts2.json') as f:
	posts_json = json.load(f)

for post in posts_json:
	post = Post(title=post['title'], content=post['content'], community=post['community'], author_id=post['user_id'])
	post.save()


