#!/usr/bin/python

import sys

sys.path.append('/homepages/10/d337401589/htdocs/modules/')

import tweetbot

def follow_by_RT(name, number):

    timeline = tweetbot.BOT.statuses.user_timeline(screen_name=name, count=1, exclude_replies='true', trim_user='true')

    last_tweet_id = timeline[0][u'id_str']

    retweets = tweetbot.BOT.statuses.retweets(id=last_tweet_id)

    for i in xrange(number):
        try:
            tweet = retweets[i]
            retweeter = tweet[u'user'][u'id']
            tweetbot.follow(retweeter)
        except:
            pass
