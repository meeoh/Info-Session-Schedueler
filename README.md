# Info-Session-Schedueler

The goal of this project is to be able to ask the student on a daily basis which info session he/she would like to participate in. It should only ask about info sessions that do not conflict (too badly, some overlap should be ok) with the students courses. It'll make use of the uwaterloo api in order to get the info session information, and find the timings of the students courses. As of right now, I can either find the students courses and then in that same script, ask the student if they would like to participate which would mean the script would have to run forever. OR I can get the students schedule, export it to a file, then run a cron job that executes once a day.

TODO: <br>

1. Get the students schedule :white_check_mark:
2. Store it somewhere (maybe) :white_check_mark:
3. Get the info sessions for the day :white_check_mark:
4. Check which oens are appropriate 
5. Ask the student (currently via telegram, can be texting via twilio or email) if they would like to participate
6. Enroll them if they say yes, ignore if no

## Usage
Create a telegram bot and get the bot http access key<br>
Set the api keys in apikeys.py<br>
Run `pip install -r requirements.txt` to install the proper dependencies<br>
Then run python schedule-maker.py and follow the instructions<br>
Find your chat id with the bot by running `find_id.py` and messaging the bot<br>
Set your chat id on line 45 of `register-session.py`<br>
Set the location of sched.txt (created from `schedule-maker.py`) on line 83 of `register-session.py`<br>
Finally, put register-session.py in /etc/cron.d/ and modify it for your appropriate time<br>
