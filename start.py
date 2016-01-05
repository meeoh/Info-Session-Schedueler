
for i in range(0,5):	
	print "Enter name for Course #%d (e.g CS 350)" % (i+1,)
	currentCourseName = raw_input()
	#error check
	while not currentCourseName:
		print "Please enter a valid course name"
		currentCourseName = raw_input()

	#hit waterloo api and find course
	#give options for what time/day they take it at
	#global 2d array of classes (array[0] is sunday, then each tuple in array[0] has 2 elements, start time and end time)




	


