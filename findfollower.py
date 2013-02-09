#!/usr/bin/python

import sys

sys.path.append('/homepages/10/d337401589/htdocs/modules/')

from twitter import *
import tweetbot
from random import choice



#FIND RANDOM FRIEND OF DR LEE
def findfollwer():

    random_friend_id = choice(tweetbot.BOT.friends.ids(screen_name=tweetbot.BOTname)[u'ids'])
    
    random_friend_name = tweetbot.BOT.users.show(user_id=random_friend_id)[u'screen_name']
    
    return random_friend_name

