import requests
from uwaterlooapi import UWaterlooAPI

API_KEY = "36802f2c7eab5943ece0bcf8eec07d5a"
uw = UWaterlooAPI(api_key=API_KEY)

print(uw.course_schedule("MAasTH","135"))

#classes = uw.courses("MAdsfdsfsTH")

#print(classes)

def getCourse():
    #get input
    currentCourse = raw_input()

    # error check
    while not currentCourse or len(currentCourse.split(' ')) != 2:          
        print "Please enter a valid course name"
        currentCourse = raw_input() 

    return currentCourse.upper()



#assuming 5 courses, loops 0-4
i = 1
enteredCourses = []
finalDates = [[] for x in range(5)]
while i <= 5:
        print "Enter name for Course #%d (e.g CS 350)" % (i)

        currentCourse = getCourse()        
        while currentCourse in enteredCourses:
            print "You've already entered that course!"
            print "Enter name for Course #%d (e.g CS 350)" % (i)
            currentCourse = getCourse()



        #split course into two parts
        courseName = currentCourse.split(' ')[0].upper()
        courseCode = currentCourse.split(' ')[1]

        classes = uw.course_schedule(courseName, courseCode)
        if not classes:
            print "Your course isnt offered at UWaterloo, try entering it again or do CTRL-C to quit"            
            continue

        enteredCourses.append(currentCourse)
       
        i = i + 1
        
        #LISTS ALL PROFS FOR THE COURSE
        index = 1
        for section in classes:
            currentSection = section
            currentSection = currentSection['classes'][0]            
            startTime = currentSection["date"]["start_time"]
            endTime = currentSection["date"]["end_time"]
            days = currentSection["date"]["weekdays"]
            if currentSection['instructors']:                
                #ALL PROFS HERE WITH TIME ALL SECTIONS INCLUDED
                currentSection = currentSection['instructors'][0]
                print  str(index) + ": " + currentSection + " " + startTime + " " + endTime + " " + days
                index = index + 1

        #need to error check this choice
        choice = int(raw_input())

        query_index = 1
        for section in classes:
            currentSection = section
            currentSection = currentSection['classes'][0]            
            startTime = currentSection["date"]["start_time"]
            endTime = currentSection["date"]["end_time"]
            days = currentSection["date"]["weekdays"]
            if currentSection['instructors'] and query_index == choice:                
                #ALL PROFS HERE WITH TIME ALL SECTIONS INCLUDED
                while len(days) > 0:
                    if "M" in days:
                        finalDates[0].append((startTime,endTime))
                        days = days.replace("M","")                    
                    elif "Th" in days:
                        finalDates[3].append((startTime,endTime))
                        days = days.replace("Th","")
                    elif "T" in days:
                        finalDates[1].append((startTime,endTime))
                        days = days.replace("T","")       
                    elif "F" in days :
                        finalDates[4].append((startTime,endTime))
                        days = days.replace("F","")
                    elif "W" in days:
                        finalDates[2].append((startTime,endTime))
                        days = days.replace("W","")
            
            query_index = query_index + 1
        #print finalDates


        #COURSE EXISTS AT THIS POINT 

        # hit waterloo api and find course

        # give options for what time/day they take it at
        '''' global 2d array of classes (array[0] is sunday, then each tuple in
        array[0] has 2 elements, start time and end time which represents an individual
        class)'''

#print enteredCourses
#print "TEST"
#print finalDates[1][0][0]
for elm in finalDates:
    elm.sort(key=lambda x:x[0])

f = open('sched.txt', 'w')
for index,elm in enumerate(finalDates):
    if index == 0:
        f.write("MONDAY\n")
    elif index == 1:
        f.write("TUESDAY\n")
    elif index == 2:
        f.write("WEDNESDAY\n")
    elif index == 3:
        f.write("THURSDAY\n")
    elif index == 4:
        f.write("FRIDAY\n")    
    for pair in elm:
        f.write(pair[0] + " " + pair[1] + "\n")


#finalDates = sorted(finalDates, key=lambda x: x[0])

