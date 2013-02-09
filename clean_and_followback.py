#!/usr/bin/python

import sys

sys.path.append('/homepages/10/d337401589/htdocs/modules/')

from twitter import *
import tweetbot


#CLEAN UP FOLLOWING LIST
def clean_and_followback(number):
    
    # set of people that lee follows
    friends_page = tweetbot.BOT.friends.ids(screen_name='drcharleslee')
    BOT_friends = set(friends_page['ids'])
    while friends_page['next_cursor_str'] != '0':
        friends_page = tweetbot.BOT.friends.ids(screen_name=tweetbot.BOTname, cursor=friends_page['next_cursor_str'])
        BOT_friends |= set(friends_page['ids'])
    
    # set of people that follow lee
    followers_page = tweetbot.BOT.followers.ids(screen_name=tweetbot.BOTname)
    BOT_followers = set(followers_page['ids'])
    while followers_page['next_cursor_str'] != '0':
        followers_page = tweetbot.BOT.followers.ids(screen_name=tweetbot.BOTname, cursor=followers_page['next_cursor_str'])
        BOT_followers |= set(followers_page['ids'])
    
    # clean people who don't follow back
    unfollowers = list(BOT_friends - BOT_followers)
    for f in unfollowers[:number]:
        try: 
            tweetbot.BOT.friendships.destroy(user_id=f)
    	except:
            pass

    # automatic follow back
    if len(BOT_followers) < 20000:
        unfollowed = list(BOT_followers - BOT_friends)
        for f in unfollowed:
            tweetbot.follow(f)


