
A = [1, 5, 2, 4, 3]

def selection_sort(A):
    #iterate through the list and find the minimum element. Then swap it with the first element. Then iterate through the rest of the list in 
    #the same way, swapping the minimum element with the next element in the list. 
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] < A[i]:
                A[i], A[j] = A[j], A[i]
    return A

print(selection_sort(A))

# This has time complexity O(n^2) in all cases. It is not stable, meaning that the relative order of elements with the
# same value is not preserved. It is in-place, meaning that it does not require any extra memory. It is not adaptive,
# meaning that it does not take advantage of existing order in the list. 

