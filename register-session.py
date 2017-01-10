import requests
import time
import datetime
from uwaterlooapi import UWaterlooAPI
import apikeys
import sys
import logging
import telegram
from time import sleep

try:
    from urllib.error import URLError
except ImportError:
    from urllib2 import URLError  # python 2

telegramChatId = 130724919


def botMessage(message):
    # Telegram Bot Authorization Token
    bot = telegram.Bot(apikeys.getTelegramBotKey())

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
    else:
        bot.sendMessage(chat_id=telegramChatId, text="No sessions today")
    return update_id


API_KEY = apikeys.getUWApiKey()
uw = UWaterlooAPI(api_key=API_KEY)


todays_sessions = []


day = int(time.strftime("%d"))

todaysDate = time.strftime("%Y") + time.strftime("-%m-") + str(day)


for event in uw.infosessions():    
    if "CANCELLED" in event["employer"].upper():
        continue
    if event["date"] == todaysDate:        
        todays_sessions.append(
            (event["employer"], event["start_time"], event["end_time"], event["id"]))


'''
todays_sessions.sort(key=lambda x: x[1])
print "TODAYS SESSIONS"
print "---------------"
print todays_sessions	

weekday = time.strftime("%A").upper()


sched = [[] for x in range(5)]

#put the location of sched.txt here
f = open('/home/pi/Info-Session-Schedueler/sched.txt', 'r')
currentDay = -1
for line in f:
	if "DAY" in line:
		currentDay = currentDay + 1
	else:		
		starting = line.split(' ')[0]
		ending = line.split(' ')[1].strip()
		sched[currentDay].append((starting, ending))			

today_as_int = datetime.datetime.today().weekday()
if today_as_int > 4:
	today_as_int = 0

todays_sched = sched[datetime.datetime.today().weekday()]
print "TODAYS CLASSES"
print "---------------"
print todays_sched
print "\n"
'''

message = ""

for session in todays_sessions:
    message = message + session[0] + " at " + \
        session[1] + " ends at " + session[2] + "\n"

botMessage(message)

# for index,session in enumerate(todays_sessions):
# 	for classIndex,classTime in enumerate(todays_sched):
#  		if session[1] < classTime[0]:
#  			print "STARTS BEFORE CLASS: " + str(classIndex)
#  			print session[0] + " starts at: " + session[1] + " and ends at " + session[2] + "."
#  			print "\n"
#  			break
