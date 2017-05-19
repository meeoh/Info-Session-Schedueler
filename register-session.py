import requests
import time
import datetime
from uwaterlooapi import UWaterlooAPI
import apikeys
import sys
import logging
import telegram
import twitter
import twitterkeys
from time import sleep

try:
    from urllib.error import URLError
except ImportError:
    from urllib2 import URLError  # python 2

telegramChatId = 130724919


def botMessage(message):
    # Telegram Bot Authorization Token
    bot = telegram.Bot(apikeys.TelegramBotKey)

    # get the first pending update_id, this is so we can skip over it in case
    # we get an "Unauthorized" exception.
    try:
        update_id = bot.getUpdates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    try:
        update_id = echo(bot, update_id, message)
    except telegram.TelegramError as e:
        # These are network problems with Telegram.
        if e.message in ("Bad Gateway", "Timed out"):
            sleep(1)
        elif e.message == "Unauthorized":
            # The user has removed or blocked the bot.
            update_id += 1
        else:
            raise e


def echo(bot, update_id, message):
    if message:
        bot.sendMessage(chat_id=telegramChatId, text=message)
	api = twitter.Api(consumer_key=twitterkeys.consumerkey, consumer_secret=twitterkeys.consumersecret, access_token_key=twitterkeys.accesstokenkey, access_token_secret=twitterkeys.accesstokensecret)
	try:
		api.PostUpdate(message)
	except:
		print("EXCEPTION")
    else:
        bot.sendMessage(chat_id=telegramChatId, text="No sessions today")
    return update_id


API_KEY = apikeys.UWApiKey
uw = UWaterlooAPI(api_key=API_KEY)


todays_sessions = []


day = int(time.strftime("%d"))

todaysDate = time.strftime("%Y") + time.strftime("-%m-") + str(day)

#get all sessions for today
for event in uw.infosessions():
    if "CANCELLED" in event["employer"].upper():
        continue
    if event["date"] == todaysDate:
        todays_sessions.append(
            (event["employer"], event["start_time"], event["end_time"], event["id"]))

#sort session by ascending time
todays_sessions.sort(key=lambda tup: tup[1])  # sorts in place

message = ""

#create the message
for session in todays_sessions:
    message = message + session[0] + " at " + \
        session[1] + " ends at " + session[2] + "\n"

#send the message
botMessage(message)
