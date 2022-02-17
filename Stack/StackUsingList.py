# Create empty stack using list
stack = []

msg = input('Want to push items in stack: press y/n ? ')
# Push items in stack
while msg == 'y':
    value = input('Enter value to push in stack ')
    stack.append(value)
    msg = input('Want to push items in stack: press y/n ? ')

print('Stack')
print(stack)

msg = input('Want to pop items in stack: press y/n ? ')
# Pop items from stack
print('Pop items')
while msg == 'y':
    if len(stack) >= 1:
        print(stack.pop())
        msg = input('Want to pop items in stack: press y/n ? ')
    else:
        print('Stack is empty')
        msg = 'n'

print('Stack')
print(stack)