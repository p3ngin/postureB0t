# cfg.py
# contains configurations for the bot

HOST = "irc.twitch.tv"
PORT = 6667
NICK = "TWITCH_BOT_ACCOUNT" #twitch account with dev API access. Sign up for access dev.twitch.tv
PASS = "oauth:INSERTOAUTHKEY" #from your twitch dev account, replace this with your oauth key
CHAN = "TARGET_TWITCH_ACCOUNT" #twitch account you want to configure postureB0t to send reminders to
RATE = (20/30) #messages per second

oplist = {}
