# Stacks and queues are dynamic sets in which a prespecified element is removed or added, respectively.
# In a stack, the most recently added element is removed first. This is called last-in, first-out (LIFO).
# In a queue, the element removed is always the one that has been in the set for the longest time. This is called first-in, first-out (FIFO).

# Stacks
stack = [2, 4, 6]
stack.append(5)
print(stack)
stack.pop()
print(stack)

# Queues
from collections import deque
queue = deque([2, 4, 6])
queue.append(5)
print(queue)
queue.popleft()
print(queue)
queue.pop()
print(queue)