import random

# Create a list of 10 random numbers
random.seed("ABC")
numbers = [random.randint(0,1000) for i in range(10)]

# Recursive mergesort function
def mergesort(arr):
    
    if len(arr) > 1:
        #split the array into two halves
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
    
        #after this, left_arr and right_arr are sorted
        mergesort(left_arr)
        mergesort(right_arr)
        
        #merge
        i = 0 # left array index
        j = 0 # right array index
        k = 0 # merged array index
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i+=1
            
            else:
                arr[k] = right_arr[j]
                j+=1
            
            k+=1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i+=1
            k+=1
            
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j+=1
            k+=1
            
    return arr

print(numbers)
print(mergesort(numbers))                

#this has complexity O(nlogn) in all cases.