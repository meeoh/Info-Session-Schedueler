# Info-Session-Schedueler

The goal of this project is to be able to ask the student on a daily basis which info session he/she would like to participate in. It should only ask about info sessions that do not conflict (too badly, some overlap should be ok) with the students courses. It'll make use of the uwaterloo api in order to get the info session information, and find the timings of the students courses. As of right now, I can either find the students courses and then in that same script, ask the student if they would like to participate which would mean the script would have to run forever. OR I can get the students schedule, export it to a file, then run a cron job that executes once a day.

TODO:
Get the students schedule
Store it somewhere (maybe)
Get the info sessions for the day
Check which oens are appropriate
Ask the student (currently via telegram, can be texting via twilio or email) if they would like to participate
Enroll them if they say yes, ignore if no
