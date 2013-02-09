#!/usr/bin/python

import sys

sys.path.append('/homepages/10/d337401589/htdocs/modules/')

import tweetbot
from random import randrange, choice, shuffle
from linecache import getline


# RETURN A RANDOM TWEET WITH TWO LINES FROM TWEETLINES.TXT
def tweet(specific=None):
    
    tweet_list = [getline('/homepages/10/d337401589/htdocs/modules/tweetbot/tweetlines.txt', randrange(tweetbot.line_count))[:-1]]
    
    # if a specific word is specified
    if specific is not None:
        matching_list = []
        
        with open('/homepages/10/d337401589/htdocs/modules/tweetbot/tweetlines.txt') as lines:
            for line in lines:
                if specific in line:
                    matching_list.append(line)
        
        if len(matching_list) == 0:
            tweet_list.append(getline('/homepages/10/d337401589/htdocs/modules/tweetbot/tweetlines.txt', randrange(tweetbot.line_count))[:-1])
        
        else:
            tweet_list.append(choice(matching_list)[:-1])

    
    # if specific is None
    else:
        tweet_list.append(getline('/homepages/10/d337401589/htdocs/modules/tweetbot/tweetlines.txt', randrange(tweetbot.line_count))[:-1])

    # put the two lines together
    shuffle(tweet_list)

    tweet_text = tweet_list[0][:-1] + ', '

    if (tweet_list[1][:2] == 'I ') or (tweet_list[1][:2] == 'Mr') or (tweet_list[1][:2].isupper() == True and ' ' not in tweet_list[1][:2]):
        tweet_text += tweet_list[1]
    else:
        tweet_text += tweet_list[1][0].lower()
        tweet_text += tweet_list[1][1:]

    return tweet_text
