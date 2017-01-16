#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import csv

#http://www.tweepy.org/
import tweepy

#Get your Twitter API credentials and enter them here
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_key = "your_access_key"
access_secret = "your_access_secret"

#method to get a user's last 100 tweets
def get_tweets(username):

	#http://tweepy.readthedocs.org/en/v3.1.0/getting_started.html#api
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	#set count to however many tweets you want; twitter only allows 200 at once
	number_of_tweets = 10

	#get tweets
	tweets = api.user_timeline(screen_name = username,count = number_of_tweets)

	tweets_for_csv = [[tweet.text.encode("utf-8")] for tweet in tweets]

	#we always want the latest tweet
	tweets_for_pi = tweets_for_csv.pop(0)

	#we want to find if tweets are in a series
	for num, tweet in enumerate(tweets_for_csv):
		firstTweet = str(tweets_for_pi)
		thisTweet = str(tweet)
		#if the next tweet starts with this '..' we want the next one too
		if firstTweet.startswith(".."):
			tweets_for_pi.insert(0,thisTweet[2:-2])
		#this is the next one in the series
		if firstTweet.startswith("..") and thisTweet.startswith("['.."):
			#debug
			print "[DEBUG] Yes for %d" % num
			tweets_for_pi.insert(0,thisTweet[2:-2])
		#another format type, this is usually the last one
		if thisTweet.endswith("..']"):
			#debug
			print "[DEBUG] Also yes for %d" % num
			tweets_for_pi.insert(0,thisTweet[2:-2])
			#but we need to see if we failed to catch one before now
			while (num > 0):
				num = num - 1
				thisTweet = str(tweets_for_pi[num])
				if thisTweet.endswith("..']"):
					tweets_for_pi.insert(0,thisTweet[2:-2])
					print "[DEBUG] Adding prev1 as well"
				else:
					tweets_for_pi.insert(0,thisTweet[2:-2])
					print "[DEBUG] Adding prev2 as well"
					break
			print "[DEBUG] it broke right"
		#if nothing else, the first one is standalone
		else:	break

	for tweet in tweets_for_pi:
		print tweet

	#the following is old and won't be used
	#create array of tweet information: username, tweet id, date/time, text
	#tweets_for_csv = [[username,tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in tweets]

	#write to a new csv file from the array of tweets
	#print "writing to {0}_tweets.csv".format(username)
	#with open("{0}_tweets.csv".format(username) , 'w+') as file:
	#	writer = csv.writer(file, delimiter='|')
	#	writer.writerows(tweets_for_csv)


#if we're running this as a script
if __name__ == '__main__':

    #get tweets for username passed at command line
    if len(sys.argv) == 2:
        get_tweets(sys.argv[1])
    else:
        print "Error: enter one username"

    #alternative method: loop through multiple users
	# users = ['user1','user2']

	# for user in users:
	# 	get_tweets(user)
