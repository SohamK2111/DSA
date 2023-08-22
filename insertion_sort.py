
#given input list of numbers A, sort using insertion sort in ascending order

A = [2, 1, 3, 5, 4, 7, 6, 9, 8, 10]

def insertion_sort(A):
    for j in range(1, len(A)):
        # The number we wish to sort is called the key
        key = A[j]
        #indicies of 0 to j-1 are already sorted so create a new variable i
        i = j - 1
        while i >= 0 and A[i] > key:
            #shift the value of A[i] to the right
            A[i+1] = A[i]
            i-=1
        #insert the key into the correct position
        A[i+1] = key
    return A
    
print(insertion_sort(A))