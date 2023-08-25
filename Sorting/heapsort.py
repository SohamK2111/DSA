import random

random.seed("abc")
A = [random.randint(-10,10) for i in range(20)]

heapsize =  len(A)

def parent(i):
    return i//2
def left(i):
    return 2*i
def right(i):
    return (2*i + 1)

def max_heapify(A, i):
    l = left(i)
    r = right(i)
    if l <= heapsize and A[l-1] > A[i-1]:
        largest = l
    else:
        largest = i
    if r <= heapsize and A[r-1] > A[largest-1]:
        largest = r
    if largest != i:
        A[i-1], A[largest-1] = A[largest-1], A[i-1]
        max_heapify(A, largest)
        
def build_max_heap(A):
    for i in range(heapsize//2, 0, -1):
        max_heapify(A, i)
        
def heapsort(A):
    global heapsize
    build_max_heap(A)
    for i in range(heapsize, 1, -1):
        A[0], A[i-1] = A[i-1], A[0]
        heapsize -= 1
        max_heapify(A, 1)
    return A
        
print(heapsort(A))

#------------------------------------------------------------

#Priority Queues

# A priority queue is a data structure for maintaining a set S of elements, each with an associated value called a key.
# A max-priority queue supports the following operations:

# heap_maximum(S) returns the element of S with the largest key
def heap_maximum(A):
    return A[0]

# heap_extract_max(S) removes and returns the element of S with the largest key and removes it from the queue
def heap_extract_max(A):
    global heapsize
    if heapsize < 1:
        print("heap underflow")
    max = A[0]
    A[0] = A[heapsize-1]
    heapsize -= 1
    max_heapify(A, 1)
    return max

# heap_increase_key(S, x, k) increases the value of element x's key to the new value k, which is assumed to be at least as large as x's current key value
def heap_increase_key(A, i, key):
    if key < A[i-1]:
        print("new key is smaller than current key")
    A[i-1] = key
    while i > 1 and A[parent(i)-1] < A[i-1]:
        A[i-1], A[parent(i)-1] = A[parent(i)-1], A[i-1]
        i = parent(i)

# max_heap_insert(S, x) inserts the element x into the set S, which is equivalent to the operation S = S U {x}
def max_heap_insert(A, key):
    global heapsize
    heapsize += 1
    A.append(-float('inf'))
    heap_increase_key(A, heapsize, key)
    return A
    

print(max_heap_insert(A, 100))
print(heap_extract_max(A))
print(A)

#------------------------------------------------------------

import heapq

# heapq is a module that provides an implementation of a min-priority queue using a binary heap
# to turn it into a max-priority queue, you can negate the keys

li = [1,2,3,4,5,6,7,8,9,10]

heapq.heapify(li)
minheap = li
print("minheap:", minheap)
heapq._heapify_max(li)
maxheap = li
print("maxheap:", maxheap)
heapq.heapify([-i for i in li])
maxheap1 = li
print("maxheap:", maxheap1)


# there are 3 main functions in heapq: heappush, heappop and heapify. For more info, see https://docs.python.org/3/library/heapq.html