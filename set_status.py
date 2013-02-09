#!/usr/bin/python

import sys

sys.path.append('/homepages/10/d337401589/htdocs/modules/')

from twitter import *
import tweetbot

#SET THE STATUS OF THE BOT TO TEXT
def set_status(text):
    tweetbot.BOT.statuses.update(status=text, trim_user='true')