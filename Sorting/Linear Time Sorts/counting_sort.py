# Assuming that each of the n input elements is an integer in the range 0 to k, for some integer k.
# Counting sort determines the number of elements below each input element. It then uses this information to place the input element directly into its position in the output array.
import numpy as np

def countingsort(A, B, k):
    # A is the input array, B is the output array, k is the maximum value of an element in A, C is the temporary array
    C = np.zeros(k+1)
    # This loop counts the number of elements in A equal to j and stores it in C[j]
    for j in range(len(A)):
        C[A[j]] += 1
    # This loop counts the number of elements less than or equal to i and stores it in C[i]
    for i in range(1, k+1):
        C[i] += C[i-1]
    # This loop places each element in A into its correct position in B
    for j in range(len(A)-1, -1, -1):
        # C[A[j]] is the number of elements less than or equal to A[j]
        B[int(C[A[j]])-1] = A[j]
        C[A[j]] -= 1
    return B

A = [2,5,3,0,2,3,0,3]
B = np.zeros(len(A))

print(countingsort(A, B, 5))

#Counting sort is stable - numbers with the same value appear in the output array in the same order as they do in the input array. 
#This is especially important when sorting objects with several keys, where you might want to sort by one key and then another.