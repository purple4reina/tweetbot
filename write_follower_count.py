#!/usr/bin/python

import sys

sys.path.append('/homepages/10/d337401589/htdocs/modules/')

from twitter import *
import tweetbot
from time import localtime


# WRITE THE NUMBER OF CURRENT FOLLOWERS OF LEE TO FILE
def write_follower_count():
    
    def num_of_followers():
        followers_page = tweetbot.BOT.followers.ids(screen_name=tweetbot.BOTname)
        BOT_followers = set(followers_page['ids'])
        while followers_page['next_cursor_str'] != '0':
            followers_page = tweetbot.BOT.followers.ids(screen_name=tweetbot.BOTname, cursor=followers_page['next_cursor_str'])
            BOT_followers |= set(followers_page['ids'])
        
        return str(len(list(BOT_followers)))
    
    with open('/homepages/10/d337401589/htdocs/modules/tweetbot/followers.txt', 'r+w+') as f_file:
        lines = f_file.readlines()

        now = localtime()
        year = str(now[0])
        month = str(now[1])
        if len(month) < 2: month = '0' + month
        day = str(now[2])
        if len(day) < 2: day = '0' + day

        date_today = str(year + '-' + month + '-' + day)
        if lines[-1][-10:] != date_today:
            f_file.write('\n' + num_of_followers() + ', ' + date_today)
