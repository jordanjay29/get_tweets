#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import time
import RPi.GPIO as GPIO
from papirus import Papirus
from papirus import PapirusText

SW1 = 26
SW2 = 19
SW3 = 20
SW4 = 16
SW5 = 21

def main()
	screen.clear()

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(SW1, GPIO.IN)
    GPIO.setup(SW2, GPIO.IN)
    GPIO.setup(SW3, GPIO.IN)
    GPIO.setup(SW4, GPIO.IN)
	GPIO.setup(SW5, GPIO.IN)

	refresh()

	while True;
		if GPIO.input(SW1) == False:
			if num > maxNum:
				num + 1
			tweet = tweets[num]
			text.write(tweet,13)

		if GPIO.input(SW2) == False:
			if num > 0:
				num - 1
			tweet = tweets[num]
			text.write(tweet,13)

		if GPIO.input(SW3) == False:
			text.write('Refreshing tweets.')
			refresh()

		if GPIO.input(SW5) == False:
			text.write('Shutting down.')
			time.sleep(2)
			screen.clear()
			os.system("sudo shutdown now")
			
		
def refresh()
	tweets = get_tweets(realDonaldTrump)
	num = 0
	maxNum = len(tweets)
	tweet = tweets[num]	

	text.write(tweet,13)	
