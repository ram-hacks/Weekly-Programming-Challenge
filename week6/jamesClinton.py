# James Clinton
# Merge Sort
# Large Data Merge Sort
# Ram Hacks Programming Challenge

# Stores the array of numbers


# Pulls in Data from the external file
def pullInData(fileName):
	# Pulls in the numbers to be sorted
	with open(fileName) as f:
		numbersList = f.readlines()
	return numbersList

# Will serve as the main mergesort function
def MergeSort(someArray):
	
	# Check to see if the array is longer than 1
    if len(someArray)>1:
		# Finds the middle
        mid = len(someArray)//2
		
		# Splits the Left and Right halves
        lefthalf = someArray[:mid]
        righthalf = someArray[mid:]

		# Recursively mergeSorts
        MergeSort(lefthalf)
        MergeSort(righthalf)

		# Lets create some variables for our while loops
        i=0
        j=0
        k=0
		
		# Will loop while i and j are less than leftHalf and rightHalf, respectively
		# Combines the two arrays in sorted order
        while i < len(lefthalf) and j < len(righthalf):
                
            if float(lefthalf[i]) < float(righthalf[j]):
                someArray[k]=lefthalf[i]
                i=i+1
            else:
                someArray[k]=righthalf[j]
                j=j+1
            k=k+1
		
		# Will fill out the list with the rest of leftHalf if ther are numbers left in items
		# *Only occurs when rightHalf Empties
        while i < len(lefthalf):
            someArray[k]=lefthalf[i]
            i=i+1
            k=k+1
		
		# Will fill out the list with the rest of rightHalf if ther are numbers left in items
		# *Only occurs when leftHalf Empties
        while j < len(righthalf):
            someArray[k]=righthalf[j]
            j=j+1
            k=k+1	



# The main function for the program
def main():
	Filename = input('Filename: ')
	numbersList = pullInData(Filename)
	MergeSort(numbersList)
	output = open('output.txt', 'w')
	#print (numbersList)
	for item in numbersList:
		output.write("%s\n" % item)
	
	


