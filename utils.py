#!usr/bin/python
# utils.py
# A bunch of utility functions

import cfg
import json
import time, threading
from time import sleep
import urllib.request as urllib2

	# Send a chat message to the server.
		# Parameters: 
		# 	sock -- the socket over which to send the message
		#	msg -- the message to send

def chat(sock, msg):
		sock.send("PRIVMSG #{} :{}\r\n".format(cfg.CHAN, msg))


def threadFillOpList():
	while True:
		try:
			url = "http://tmi.twitch.tv/group/user/" + cfg.CHAN + "/chatters"
			req = urllib2.Request(url, headers={"accept": "*/*"})
			response = urllib2.urlopen(req).read
			if response.find("502 Bad Gateway") == -1:
				cfg.oplist.clear()
				data = json.loads(response)
				for p in data ["chatters"] ["moderators"]:
					cfg.oplist[p] = "mod"
		except:
				'do nothing'
		sleep(5)

def isOp(user):
	return user in cfg.oplist
