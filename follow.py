#!/usr/bin/python

import sys

sys.path.append('/homepages/10/d337401589/htdocs/modules/')

from twitter import *
import tweetbot


def follow(id):
    try:
        tweetbot.BOT.friendships.create(user_id=id)
    except:
        pass