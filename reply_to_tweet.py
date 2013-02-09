#!/usr/bin/python

import sys

sys.path.append('/homepages/10/d337401589/htdocs/modules/')

import tweetbot

def reply_to_tweet(text, tweetid):
    tweetbot.BOT.statuses.update(status=text, in_reply_to_status_id=tweetid, trim_user='true')