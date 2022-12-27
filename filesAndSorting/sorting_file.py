
import csv #import csv module
import numpy as np

def bubbleSort(A):
    indexingLength = len(A) - 1  #do not apply comparison w last item of list. Len is length.
    sorted = False  # break out when list has been sorted
    while not sorted: #as long as sorted is False will perform this action.
        sorted = True
        for i in range(0, indexingLength):
            # when sorted all variables if statement not execute & sorted variable remain true & break out of while loop
            if A[i] > A[i + 1]: #if item left is greater than item to right, then say:
                sorted = False #say sorted variable is false
                A[i], A[i + 1] = A[i + 1], A[i] #swap 2 values.
    print("Using bubble sort implementation the sorted array is:")
    print(A)
    return A

def insertionSort(A):
    indexingLength = range(1, len(A)) #all values after 1st value bc there is no value to left
    for i in indexingLength: #for every value in indexingLength:
        sortValue = A[i]  #value to sort one by one in indexing length and taking value to sort them

        while A[i - 1] > sortValue and i > 0: #also says greater than 0 bc python allows negative indexing
            # if value to left is greater than sortValue then switch
            A[i], A[i - 1] = A[i - 1], A[i]
            i = i - 1 #continue comparisons on list
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
        for j in range(i + 1, len(A)): #all elements to right of where currently are in indexing length
            # select the minimum element in every iteration
            # if list a in current position,
            if A[j] < A[minimum]:
                # going through all element
                # to right of current position on index & if find
                minimum = j # smaller value, change to minimum value
        if minimum != i: #if find item that has lower value than
        # default value, then switch those items
            A[minimum], A[i] = A[i], A[minimum] #switch item position
    print('The array after sorting by selection sort in ascending order is: ')
    print(A)
    return(A)


#main program
with open('RandomNames7000.csv', 'r') as csv_file: #'r' is to read the csv file
    id = []
    csv_reader = csv.reader(csv_file, delimiter = ',') #read the file using reader method. 'csv_file' is being passed into reader method.
    for row in csv_reader: #for row in variable
            id = [row[0] for row in csv_reader] #id is first colomn

b = bubbleSort(id)
i = insertionSort(id)
s = selectionSort(id)
#print(b)
#print(i)
#print(s)
x = np.array(b, dtype=[('int', int)])
y = np.array(i, dtype=[('int', int)])
z = np.array(s, dtype=[('int', int)])
np.savetxt('file.csv', x, delimiter=',') #save array in text file
np.savetxt('file.csv', y, delimiter=',')
np.savetxt('file.csv', z, delimiter=',')
