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