import requests
import time
import datetime
from uwaterlooapi import UWaterlooAPI

API_KEY = "36802f2c7eab5943ece0bcf8eec07d5a"
uw = UWaterlooAPI(api_key=API_KEY)


todays_sessions = []



day = int(time.strftime("%d"))

todaysDate = time.strftime("%B ") + str(day) + time.strftime(", %Y")


for event in uw.infosessions():	
	if event["date"] == todaysDate:					
		event["start_time"] = time.strftime("%H:%M", time.strptime(event["start_time"], "%I:%M %p"))
		event["end_time"] = time.strftime("%H:%M", time.strptime(event["end_time"], "%I:%M %p"))
		todays_sessions.append((event["employer"], event["start_time"], event["end_time"]))


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

# for session in todays_sessions:
# 	for classTime in todays_sched:
# 		if session[1] < classTime[0]:
			




