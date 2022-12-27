#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#

def bubbleSort(A):
    indexingLength = len(A) - 1  # len is length
    sorted = False  # break out when list or 'A' has been sorted
    while not sorted:
        sorted = True
        for i in range(0, indexingLength):
            # if value to left is greater than value to right then
            # say sorted variable is false & then swap the two values
            # then sorted variable will stay true and break out of while loop
            if A[i] > A[i + 1]:
                sorted = False
                A[i], A[i + 1] = A[i + 1], A[i]
    print("Using bubble sort implementation the sorted array is:")
    print(A)
    return A


def insertionSort(A):
    indexingLength = range(1, len(A))
    for i in indexingLength:
        sortValue = A[i]  # value to sort

        while A[i - 1] > sortValue and i > 0:
            # if value is greater than sortValue then switch
            A[i], A[i - 1] = A[i - 1], A[i]
            i = i - 1
    print('Using the insertion sort implementation, the result is:')
    print(A)
    return A


def selectionSort(A):
    indexLength = range(0, len(A)-1) # minus '1' bc have
    # 1 item left in unsorted list, assume is highest
    # value bc last item left
    for i in indexLength:
        minimum = i #ea time iterate, want 1st element
        # in unsorted list to be default minimum -> need to do comparisons
        for j in range(i + 1, len(A)):
            # select the minimum element in every iteration
            if A[j] < A[minimum]: #going through all element
                # to right of current position on index & if find
                #  smaller value, change to minimum value
                minimum = j
        if minimum != i: #if find item that has lower value than
        # default value, then switch those items
            A[minimum], A[i] = A[i], A[minimum]
    print('The array after sorting by selection sort in ascending order is: ')
    print(A)
    return(A)



