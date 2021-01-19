#!usr/bin/python
# bot.py
# The code for postureB0t

''' TO-DO: 
	- Channel command to add new streams to cfg.py file
	- Function to check each name in a list from cfg.py
'''

import cfg
import utils
import socket
import re
import requests
import json
import time, thread
from time import sleep

def is_stream_live():
	
	isLive = 0

	# Check if stream is live using twitch API and list of Channels in cfg.py
	streamer_name = cfg.CHAN
	client_id = "CLIENT_ID_TWITCH_DEV_ACCOUNT" #insert the client id from the twitch account posting reminders. Needs to have dev API access with twitch
		
	twitch_api_stream_url = "https://api.twitch.tv/kraken/streams/" \
		+ streamer_name + "?client_id=" + client_id

	streamer_html = requests.get(twitch_api_stream_url)
	streamer = json.loads(streamer_html.content)

	if streamer["stream"] != None:
		isLive = 1
		print("Streamer is live.")
		posReminder(isLive)
	else:
		isLive = 0
		print("Streamer is not Live.")
		sleep(900)
		is_stream_live()

	print(isLive)
	return isLive



def posReminder(isLive):
	# function to post a reminder to Twitch channel specified in cfg.py only if a stream is live
	# will post every 1 hour as long as channel is still live

	# Networking functions
	s = socket.socket()
	s.connect((cfg.HOST, cfg.PORT))
	s.send("PASS {}\r\n".format(cfg.PASS).encode("utf-8"))
	s.send("NICK {}\r\n".format(cfg.NICK).encode("utf-8"))
	s.send("JOIN #{}\r\n".format(cfg.CHAN).encode("utf-8"))

	CHAT_MSG = re.compile(r"^:\w+!\w@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
	
	# message that will post to Twitch channel
	utils.chat(s, "Sit up straight and consider your posture.")

	sleep(3600)

	is_stream_live()


if __name__ == "__main__":
	is_stream_live()
	
