import random

def selectionSort(original):

	#Make a copy of the list to sort
	a = []
	for i in range(0, len(original)):
		a.append(original[i])

	small = 0
	smallIndex = 0

	for i in range (0,len(a)):

		#Sets the minimum to the first non sorted location
		small = a[i]

		#Search the rest of the list for the smallest value
		for j in range(i,len(a)):

			#Found a new smallest? record its location too.
			if a[j] <= small:
				small = a[j]
				smallIndex = j

		#Make the swap
		a[smallIndex] = a[i]
		a[i] = small

	#return the copy
	return a

def main():

	#Generate a random list
	myList = []
	for i in range(0, 10):
		myList.append(random.randint(0, 20))

	sortedList = selectionSort(myList)

	print(myList)
	print(sortedList)

main()