#!/usr/bin/python

import sys

sys.path.append('/homepages/10/d337401589/htdocs/modules/')

from twitter import *
import tweetbot
from random import shuffle


#FOLLOW X NUMBER OF PEOPLE WHO FOLLOW @SOMEONE
def add_new_followers(someone, number):
     
    someone_followers = tweetbot.BOT.followers.ids(screen_name=someone)[u'ids']
    shuffle(someone_followers)
    
    for i in xrange(number):
        tweetbot.follow(someone_followers[i])
