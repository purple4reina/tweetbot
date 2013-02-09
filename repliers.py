#!/usr/bin/python

import sys

sys.path.append('/homepages/10/d337401589/htdocs/modules/')

from twitter import *
import tweetbot


#RETURNS A LIST OF SCREEN NAMES OF WHO REPLIED TO BOT RECENTLY
def repliers():
    
    replier_set = set()
    
    tweet_list = tweetbot.BOT.search.tweets(q='@' + tweetbot.BOTname, result_type='recent')[u'statuses']
    
    for i in xrange(len(tweet_list)):
        replier_set.add(str(tweet_list[i][u'user'][u'screen_name']))

    return list(replier_set)