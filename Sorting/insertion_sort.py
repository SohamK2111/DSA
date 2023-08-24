
#given input list of numbers A, sort using insertion sort in ascending order

A = input("Enter a list of numbers:")
A = list(map(int, A.split(",")))

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

# Can show correctness of insertion sort by loop invariants, which are like proofs by induction in maths. You prove
# that the algorithm is correct before the first loop (initialisation), that the algorithm is correct before the next
# iteration of the loop (maintenance) and that the algorithm is correct after the loop (termination).

# This algorithm is O(n^2) in the worst case, but O(n) in the best case (when the list is already sorted). 