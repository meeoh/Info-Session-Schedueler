import requests
import time
import datetime
from uwaterlooapi import UWaterlooAPI
import logging
import telegram
from time import sleep

try:
    from urllib.error import URLError
except ImportError:
    from urllib2 import URLError  # python 2

def botMessage(message):
    # Telegram Bot Authorization Token
    bot = telegram.Bot("167469051:AAElg9Rdrj1YTwRJxEVh4WpqaGw8GeDDpS0")

    # get the first pending update_id, this is so we can skip over it in case
    # we get an "Unauthorized" exception.
    try:
        update_id = bot.getUpdates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


    try:
        update_id = echo(bot, update_id,message)
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
    bot.sendMessage(chat_id=130724919,text=message)
    return update_id



API_KEY = "36802f2c7eab5943ece0bcf8eec07d5a"
uw = UWaterlooAPI(api_key=API_KEY)


todays_sessions = []



day = int(time.strftime("%d"))

todaysDate = time.strftime("%B ") + str(day) + time.strftime(", %Y")


for event in uw.infosessions():	
	if "CANCELLED" in event["employer"].upper():
		continue
	if event["date"] == todaysDate:						
		event["start_time"] = time.strftime("%H:%M", time.strptime(event["start_time"], "%I:%M %p"))
		event["end_time"] = time.strftime("%H:%M", time.strptime(event["end_time"], "%I:%M %p"))
		todays_sessions.append((event["employer"], event["start_time"], event["end_time"], event["id"]))


todays_sessions.sort(key=lambda x: x[1])
print "TODAYS SESSIONS"
print "---------------"
print todays_sessions	

weekday = time.strftime("%A").upper()


sched = [[] for x in range(5)]

f = open('sched.txt', 'r')

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

message = ""

for session in todays_sessions:
	message = message + session[0] + " at " + session[1] + " ends at " + session[2] + "\n"

print "TESTING"
print message


botMessage(message)

# for index,session in enumerate(todays_sessions):
# 	for classIndex,classTime in enumerate(todays_sched):
#  		if session[1] < classTime[0]:
#  			print "STARTS BEFORE CLASS: " + str(classIndex)
#  			print session[0] + " starts at: " + session[1] + " and ends at " + session[2] + "."
#  			print "\n"
#  			break

			




