# Info-Session-Schedueler

The goal of this project is to be able to ask the student on a daily basis which info session he/she would like to participate in. ~~It should only ask about info sessions that do not conflict (too badly, some overlap should be ok) with the students courses.~~ It'll make use of the uwaterloo api in order to get the info session information, and find the timings of the students courses. As of right now, I can either find the students courses and then in that same script, ask the student if they would like to participate which would mean the script would have to run forever. OR I can get the students schedule, export it to a file, then run a cron job that executes once a day.

EDIT:
I've decided to leave out the part that only asks for info sessions that dont conflict with classes. This is because some info sessions are more important then attending a class. Also, enrolling doesnt need to be implemented since you can just show up and be fine.

TODO: <br>

1. Get the students schedule :white_check_mark:
2. Store it somewhere (maybe) :white_check_mark:
3. Get the info sessions for the day :white_check_mark:
4. Tell the student the info sessions and timing :white_check_mark:

~~4. Check which ones are appropriate <br>
5. Ask the student (currently via telegram, can be texting via twilio or email) if they would like to participate <br>
6. Enroll them if they say yes, ignore if no~~

## Usage
Create a telegram bot and get the bot http access key<br>
Set the api keys in apikeys.py<br>
Run `pip install -r requirements.txt` to install the proper dependencies<br>
~~Then run python schedule-maker.py and follow the instructions<br>~~
Find your chat id with the bot by running `find_id.py` and messaging the bot<br>
Set your chat id on line 16 of `register-session.py`<br>
~~Set the location of sched.txt (created from `schedule-maker.py`) on line 83 of `register-session.py`<br>~~
Finally, run `crontab -e` and create the appropriate job to run register-session.py at your preferred time
