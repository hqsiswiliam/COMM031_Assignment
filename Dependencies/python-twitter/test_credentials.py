import twitter
api = twitter.Api()
api = twitter.Api(consumer_key='1y4WdNqMIpNYkAn1nxaXK7eXo',
	consumer_secret='3AeL5gLcjyc6XOrKNQ6e1vIjl5Z9ZiPnaJ1d6kLh2fI4TlDpVi',
	access_token_key='2231668399-UIw0huKnGjBSJRkMxFSPjG6Ms5pYL4NnrFouTb0', 
	access_token_secret='CtBsvWiYR45zUG6kZGLX51507C8ql7BKRIMWprwF0jBhA')
users = api.GetFriends()