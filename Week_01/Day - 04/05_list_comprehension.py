"""
Concept: List Comprehension
Compact syntax for loops with conditions
"""

# Squares of even numbers from 1 to 10
squares = [x**2 for x in range(1, 11) if x % 2 == 0]

print("Squares of even numbers:", squares)
