"""
Concept: Stack Emulator
Stack follows LIFO (Last In, First Out)
append() -> push
pop() -> remove last
"""

stack = []

stack.append(1)
stack.append(2)
stack.append(3)

print("Stack:", stack)

last_item = stack.pop()
print("Popped item:", last_item)
print("Stack after pop:", stack)
