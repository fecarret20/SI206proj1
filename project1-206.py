import os
import filecmp
from dateutil.relativedelta import *
from datetime import date


def getData(file):
# get a list of dictionary objects from the file
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows
	
	#Open file and skip first row then close it
	inFile = open(file, 'r')
	next(inFile)
	lines = inFile.readlines()
	inFile.close()

	listDict = list()

	#parse the csv for separate key values
	for line in lines:
		dataDict = dict()
		vals = line.split(",")
		first = vals[0]
		last = vals[1]
		email = vals[2]
		grade = vals[3]
		dob = vals[4]

		#assign the key values to the key
		dataDict["First"] = first
		dataDict["Last"] = last
		dataDict["Email"] = email
		dataDict["Year"] = grade
		dataDict["DOB"] = dob

		#add the dictionary to the list
		listDict.append(dataDict)

	return listDict

def mySort(data,col):
# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName
	#sorts the data based on the key
	sortedData = sorted(data, key=lambda k: k[col])

	return sortedData[0]["First"] + " " + sortedData[0]["Last"]

def classSizes(data):
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]
	
	numFreshman = 0
	numSophomore = 0
	numJunior = 0
	numSenior = 0

	counter = 0

	#Calculate frequencies of each year
	while counter < len(data):
		if data[counter]["Year"] == "Freshman":
			numFreshman += 1

		elif data[counter]["Year"] == "Sophomore":
			numSophomore += 1

		elif data[counter]["Year"] == "Junior":
			numJunior += 1

		elif data[counter]["Year"] == "Senior":
			numSenior += 1

		counter += 1

	#Store them as a list of tuples
	histo = [("Freshman", numFreshman), ("Sophomore", numSophomore), 
	("Junior", numJunior), ("Senior", numSenior)]

	#sort the list ascending
	sortedHisto = sorted(histo, key=lambda tup: tup[1], reverse=True)

	return sortedHisto


def findMonth(a):
# Find the most common birth month form this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data
	dateInfo = list()

	counter = 0

	#iterate through the list and get all the months
	while counter < len(a):
		vals = a[counter]["DOB"].split("/")
		month = vals[0]

		dateInfo.append(int(month))
		counter += 1

	dateInfo.sort(reverse=True)

	maxCount = 0
	maxVal = dateInfo[0]

	#determine which month is most frequent in the data
	for item in dateInfo:
		if dateInfo.count(item) >= maxCount:
			maxCount = dateInfo.count(item)
			maxVal = item

	return maxVal

def mySortPrint(a,col,fileName):
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written
	outFile = open(fileName, 'w')
	sortedData = sorted(a, key=lambda k: k[col])

	for item in sortedData:
		line = item["First"] + "," + item["Last"] + "," + item["Email"]
		outFile.write(line)
		outFile.write("\n")



	return




def findAge(a):
# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.

	pass


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
