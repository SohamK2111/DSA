# Worst case running time of quicksort is O(n^2) but the expected running time is O(nlogn) and it sorts in place.
# it employs a divide and conquer strategy. 

def quicksort(A):
    if len(A) <= 1:
        return A
    else:
        pivot = A[0]
        less = [i for i in A[1:] if i <= pivot]
        greater = [i for i in A[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    
import random
random.seed("abc")
A = [random.randint(-100,100) for i in range(10)]

print(A)
print(quicksort(A))
