
def max_crossing_subarray(A, low, mid, high):
    leftsum = -float('inf')
    sum  = 0
    for i in range(mid, low-1, -1):
        sum += A[i]
        if sum > leftsum:
            leftsum = sum
            maxleft = i
            
    rightsum = -float('inf')
    sum = 0
    for j in range(mid+1, high+1):
        sum += A[j]
        if sum > rightsum:
            rightsum = sum
            maxright = j
    
    return (maxleft, maxright, leftsum + rightsum)

def max_subarray(A, low, high):
    if high == low:
        return (low, high, A[low])
    else:
        mid = (low + high)//2
        (leftlow, lefthigh, leftsum) = max_subarray(A, low, mid)
        (rightlow, righthigh, rightsum) = max_subarray(A, mid+1, high)
        (crosslow, crosshigh, crosssum) = max_crossing_subarray(A, low, mid, high)
        if leftsum >= rightsum and leftsum >= crosssum:
            return (leftlow, lefthigh, leftsum)
        elif rightsum >= leftsum and rightsum >= crosssum:
            return (rightlow, righthigh, rightsum)
        else:
            return (crosslow, crosshigh, crosssum)
        
import random
random.seed("abc")
A = [random.randint(-100,100) for i in range(6)]
print(A)
print(max_subarray(A, 0, len(A)-1))
# this returns the minimum and maximum indicies of the subarray and the total sum of the subarray
# the time complexity of this algorithm is O(nlogn)A