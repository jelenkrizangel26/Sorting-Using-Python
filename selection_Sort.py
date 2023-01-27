# Python program for implementation of Selection sort.

def selectionSort(array, size):
	
	for ind in range(size):
		min_index = ind

		for j in range(ind + 1, size):
			# select the minimum element in every iteration
			if array[j] < array[min_index]:
				min_index = j
		# swapping the elements to sort the array
		(array[ind], array[min_index]) = (array[min_index], array[ind])

		print(array)

arr = [64, 14, 85, 36, 19, 78, 77, 24, 27, 13]
print("\n")
print("Sorting process")
print(arr)

size = len(arr)
selectionSort(arr, size)
print("\n")
print('The array after sorting in Ascending Order by selection sort is:')
for i in range(len(arr)):
	print("% d" % arr[i], end=" ")
#Code by GeeksforGeeks