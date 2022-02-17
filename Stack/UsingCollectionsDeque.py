# Python stack can be implemented using the deque class from the collections module
from collections import deque

stack = deque()

msg = input('Wants to push items in stack: press y/n ? ')
# Push items in stack
while msg == 'y':
    push_items = input('Enter items to push in stack ')
    stack.append(push_items)
    msg = input('Wants to push items in stack: press y/n ? ')

print('Stack')
print(stack)

# Pop items from stack
msg = input('Wants to pop items from stack: press y/n ? ')
while msg == 'y':
    if len(stack) >= 1:
        pop_item = stack.pop()
        print(pop_item)
        msg = input('Wants to pop items from stack: press y/n ? ')
    else:
        print('Stack is empty')
        msg = 'n'

print('Stack')
print(stack)