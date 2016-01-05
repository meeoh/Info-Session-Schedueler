import requests


API_KEY = "?key=36802f2c7eab5943ece0bcf8eec07d5a"


if __name__ == "__main__":

	for i in range(0, 5):
	    print "Enter name for Course #%d (e.g CS 350)" % (i + 1,)
	    currentCourse = raw_input()
	    # error check
	    while not currentCourse or len(currentCourse.split(' ')) != 2:	    	
        	print "Please enter a valid course name"
        	currentCourse = raw_input()

    	courseName = currentCourse.split(' ')[0].lower()
    	courseCode = currentCourse.split(' ')[1]

    	# hit waterloo api and find course

    	# give options for what time/day they take it at
    	# global 2d array of classes (array[0] is sunday, then each tuple in
    	# array[0] has 2 elements, start time and end time)
