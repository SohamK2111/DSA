#bubble sort repeatedly swaps adjacent elements if they are in wrong order
import random

random.seed("abc")
numbers = [random.randint(0,1000) for i in range(10)]

def bubblesort(arr):
    # iterate up through indices in the array
    for i in range(1,len(arr)):
        # for each of these indices, iterate down through the array and swap numbers if they are in the wrong order
        for j in range(len(arr)-1, i-1, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

print(numbers)
print(bubblesort(numbers))

# This algorithm is O(n^2) in the worst case, but O(n) in the best case (if the array is already sorted)


