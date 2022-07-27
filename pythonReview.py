
title=input('whats your title')
description=input('write description for your video')


def create_youtube_video (title,description):
	video = {"title":title,"description":description,"likes":0,"dislikes":0,"comment":{username: comment_text}}	
def likes (video):
	if "likes" in video :
		video["likes"]= video["likes"] + 1
def dislikes (video):
	if "dislikes" in video :
		video["dislikes"]= video["dislikes"] + 1

def add_comment (video,username,comment_text):
	username=input('what is your username')
	comment_text=input('add a comment text')

	
