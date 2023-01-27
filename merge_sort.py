# Python program for implementation of Merge Sort


def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

        print(array)


# Driver program
if __name__ == '__main__':
    array = [64, 14, 85, 36, 19, 78, 77, 24, 27, 13]
    print("\n")
    print("Sorting process")
    print(array)

    mergeSort(array)

    print("\n")
    print('The array after sorting in Ascending Order by Merge sort is :')
    for i in range(len(array)):
	    print("% d" % array[i], end=" ")