------------------------
built in variables:

tweetbot.line_count  gives the number of lines of text in tweetlines.txt

tweetbot.BOT  is the access point to the twitter api as in the twitter module

tweetbot.BOTname  gives the screen name of the authenticating user


------------------------
required files:

booksample.txt  storage spot for all the books to pull text from

followers.txt  track the number of followers the bot has each day

keys.txt  here is where the api secret keys go, they are not stored elsewhere for security and ability to use this module again, the second line is the screen name of the bot

tweetlines.txt  when booksample is broken into choice sentences, they are stored here


------------------------
built in functions:

add_new_followers(screen_name, number)  follows number of people who follow screen_name

auto_reply()  replies to each mention of the bot received since the last auto reply message

clean_and_followback(number)  unfollows a number of people who do not follow the bot, follows back everyone the bot does not already follow, will not follow back when bot has more than 20k followers

cleanbooks()  takes the text from booksample.txt and grabs the choice sentences and appends them to tweetlines.txt, all sentences have at least one verb as found in the 31K verbs file

findfollower()  returns a random follower of the bot as screen_name

follow_by_RT(screen_name, number)  finds the most recent tweet by the screen_name user then follows the number of users who have retweeted that tweet

follow(user_id)  follows the user with id user_id

repliers()  returns a list of screen names of people who replied to the bot recently, as defined by twitter

reply_to_tweet(text, id)  sends a text reply to tweet with id

set_status(text)  sets the status of the bot to text, aka tweeting

specificTweet(word)  creates a tweet using a specific word included, if word not found, returns None, now deprecated in favor of tweet()

tweet(specific=None)  finds a random tweet text from the tweetlines.txt file, if specific variable is specified, that string will be included in the tweet

write_follower_count()  checks to see if the follower count has been written to followers.txt yet today, if not appwrites the number of followers of the bot to the file


------------------------
also included:

parts_of_speech_word_files  files containing large lists of words of all parts of speech
