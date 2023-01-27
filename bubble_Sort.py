# Python program for implementation of Bubble Sort

def bubbleSort(arr):
	n = len(arr)
	# optimize code, so if the array is already sorted, it doesn't need
	# to go through the entire process
	swapped = False
	# Traverse through all array elements
	for i in range(n-1):
		# range(n) also work but outer loop will
		# repeat one time more than needed.
		# Last i elements are already in place
		for j in range(0, n-i-1):

			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if arr[j] > arr[j + 1]:
				swapped = True
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
		
		if not swapped:
			# if we haven't needed to make a single swap, we
			# can just exit the main loop.
			return


# Driver code to test above
arr = [64, 14, 85, 36, 19, 78, 77, 24, 27, 13]
print("Unsorted Array")
print(arr)

bubbleSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
	print("% d" % arr[i], end=" ")

#Special thanks to GeeksforGeeks