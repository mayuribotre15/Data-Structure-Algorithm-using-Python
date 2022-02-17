# Stack in Python
A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner.

## The functions associated with stack are:

empty() – Returns whether the stack is empty – Time Complexity: O(1)
size() – Returns the size of the stack – Time Complexity: O(1)
top() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
pop() – Deletes the topmost element of the stack – Time Complexity: O(1)

Stack in Python can be implemented using the following ways: 

1. list
2. Collections.deque
3. queue.LifoQueue

### 1. Implementation using list:
Python’s built-in data structure list can be used as a stack. Instead of push(), append() is used to add elements to the top of the stack while pop() removes the element in LIFO order. 
Unfortunately, the list has a few shortcomings. The biggest issue is that it can run into speed issues as it grows. The items in the list are stored next to each other in memory, if the stack grows bigger than the block of memory that currently holds it, then Python needs to do some memory allocations. This can lead to some append() calls taking much longer than other ones.

### 2. Implementation using collections.deque:
Python stack can be implemented using the deque class from the collections module. Deque is preferred over the list in the cases where we need quicker append and pop operations from both the ends of the container, as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity. 
The same methods on deque as seen in the list are used, append() and pop().

### 3. Implementation using queue module
Queue module also has a LIFO Queue, which is basically a Stack. Data is inserted into Queue using the put() function and get() takes data out from the Queue. 

There are various functions available in this module: 

maxsize – Number of items allowed in the queue.
empty() – Return True if the queue is empty, False otherwise.
full() – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
get() – Remove and return an item from the queue. If the queue is empty, wait until an item is available.
get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
put_nowait(item) – Put an item into the queue without blocking.
qsize() – Return the number of items in the queue. If no free slot is immediately available, raise QueueFull.

### 4. Implementation using singly linked list:
The linked list has two methods addHead(item) and removeHead() that run in constant time. These two methods are suitable to implement a stack. 

getSize()– Get the number of items in the stack.
isEmpty() – Return True if the stack is empty, False otherwise.
peek() – Return the top item in the stack. If the stack is empty, raise an exception.
push(value) – Push a value into the head of the stack.
pop() – Remove and return a value in the head of the stack. If the stack is empty, raise an exception.
