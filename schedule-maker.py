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
        for section in classes:
            currentSection = section
            currentSection = currentSection['classes'][0]
            #print currentSection
            startTime = currentSection["date"]["start_time"]
            endTime = currentSection["date"]["end_time"]
            if currentSection['instructors']:
                #ALL PROFS HERE WITH TIME ALL SECTIONS INCLUDED
                currentSection = currentSection['instructors'][0]
                print currentSection + " " + startTime + " " + endTime

        #COURSE EXISTS AT THIS POINT 

        # hit waterloo api and find course

        # give options for what time/day they take it at
        '''' global 2d array of classes (array[0] is sunday, then each tuple in
        array[0] has 2 elements, start time and end time which represents an individual
        class)'''

print enteredCourses
