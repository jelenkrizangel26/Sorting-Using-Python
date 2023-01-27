# # Python program for implementation of Bubble sort.
def bubbleSort(array):
    
  # loop to access each array element
  for i in range(len(array)):

    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp
        print(array)


arr = [64, 14, 85, 36, 19, 78, 77, 24, 27, 13]

print("Sorting Process:")
bubbleSort(arr)

print("\n")
print('The array after sorting in Ascending Order by bubble sort is :')
for i in range(len(arr)):
	print("% d" % arr[i], end=" ")