#!/usr/bin/python

import sys

sys.path.append('/homepages/10/d337401589/htdocs/modules/')

import tweetbot
import shelve


def auto_reply():
    
    # open storage file
    storage = shelve.open('/homepages/10/d337401589/htdocs/modules/tweetbot/replied_mentions.dat')

    
    # retrieve the id of the last mention, then use this to get all mentions since that one
    try:
        storage['last_id']
    except:
        storage['last_id'] = '1'
    finally:
        all_mentions = tweetbot.BOT.statuses.mentions_timeline(since_id=storage['last_id'], include_rts='false')


    # create a list of screen names for those who have mentioned
    mentioners_names = []
    for this_mention in all_mentions:
        mentioners_names.append(this_mention[u'user'][u'screen_name'])


    # retrive ids of these mentions
    mention_ids = []
    for i in xrange(len(all_mentions)):
        mention_ids.append(all_mentions[i][u'id_str'])


    # store last mention for later use
    try:
        storage['last_id'] = str(mention_ids[0])
    except:
        pass


    # close storage file
    storage.close()


    # reply to each
    for i in xrange(len(all_mentions)):
        tweetbot.reply_to_tweet('@' + mentioners_names[i] + ' ' + tweetbot.tweet(), mention_ids[i])



