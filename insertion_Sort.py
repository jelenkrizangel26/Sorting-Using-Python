# Python program for implementation of Insertion sort 


def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key
        print(array)


arr = [64, 14, 85, 36, 19, 78, 77, 24, 27, 13]

print("\n")
print("Sorting Process:")
insertionSort(arr)

print("\n")
print('The array after sorting in Ascending Order by insertion sort is :')
for i in range(len(arr)):
	print("% d" % arr[i], end=" ")