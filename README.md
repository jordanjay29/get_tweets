#get_tweets.py: Python Script to download and display latest tweet (or tweets if series) on a PaPiRus eInk screen

##Features
Uses the PaPiRus combined with the Raspberry Pi to display the latest tweet or tweets from a particular user. 
Navigate forward and backward within tweet series *(coming soon, currently just auto-loops)*
Display UI on screen for easier button usage *(coming soon)*

##Requirements

Raspberry Pi Zero (could also use any Pi B or 3)
PaPiRus eInk Screen Zero (probably will work for the regular pi size with some tweaks, esp. buttons)
Twitter account
Network connection (wifi or ethernet adapter)

##Installation & How To Use

Set up your Raspberry Pi Zero and PaPiRus. The zero needs the 2x20 male pin GPIO headers soldered before the PaPiRus can be attached. 
Install PaPiRus drivers and software from (https://github.com/PiSupply/PaPiRus/). 
Install tweepy via pip (and python-pip if necessary).
Run the following code:
```'''```
$ git clone https://github.com/jordanjay29/get_tweets.git
$ cd get_tweets
```
Then you need to get your Twitter API Credentials by creating a new app at apps.twitter.com. 
Create a file named `keys.py` with the following code:

```'''```
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_key = "your_access_key"
access_secret = "your_access_secret"
```

Then you can run the script by entering one username at the command line:

```'''```
$ python get_tweets.py [twitter_username]
```

Tweets should display on your PaPiRus eink screen. 
