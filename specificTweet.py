#!/usr/bin/python

import sys

sys.path.append('/homepages/10/d337401589/htdocs/modules/')

import tweetbot
from random import shuffle, choice, randrange
from linecache import getline


# RETURN TWEET WITH SPECIFIC WORDING
def specificTweet(word):
    
    matching_list = []
    
    with open('/homepages/10/d337401589/htdocs/modules/tweetbot/tweetlines.txt') as lines:
        for line in lines:
            if word in line:
                matching_list.append(line)

    if len(matching_list) == 0:
        return

    else:
        tweet_list = []
        tweet_list.append(choice(matching_list)[:-1])
        tweet_list.append(getline('/homepages/10/d337401589/htdocs/modules/tweetbot/tweetlines.txt', randrange(tweetbot.line_count))[:-1])

        shuffle(tweet_list)
        return ' '.join(tweet_list)

        

