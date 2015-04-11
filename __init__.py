#!/usr/bin/python

import sys

sys.path.append('/homepages/10/d337401589/htdocs/modules/')

import ast
from twitter import *
from add_new_followers import *
from clean_and_followback import *
from cleanbooks import *
from findfollower import *
from repliers import *
from specificTweet import *
from tweet import *
from write_follower_count import *
from set_status import *
from follow import *
from follow_by_RT import *
from auto_reply import *
from reply_to_tweet import *
from get_amazon_link import *


# define the tuple of twitter keys from saved file
with open('/homepages/10/d337401589/htdocs/modules/tweetbot/keys.txt') as keys:
    for line in keys:
        twitter_keys = ast.literal_eval(line)
        break

# authenticate with the twitter api
BOT = Twitter(auth=OAuth(twitter_keys[0], twitter_keys[1], twitter_keys[2], twitter_keys[3]), domain='api.twitter.com', api_version='1.1')

# count the number of lines in tweetlines.txt
line_count = 0
with open('/homepages/10/d337401589/htdocs/modules/tweetbot/tweetlines.txt') as lines:
    for l in lines:
        line_count += 1

# the screen name of the bot to control
with open('/homepages/10/d337401589/htdocs/modules/tweetbot/keys.txt') as keys:
    for line in keys:
        if line[0] == '(':
            continue
        else:
            BOTname = line



