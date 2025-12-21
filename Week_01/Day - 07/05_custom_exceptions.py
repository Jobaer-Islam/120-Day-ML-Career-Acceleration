"""
Concept: Custom Exceptions
Manually enforce business rules.
"""

try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise ValueError("No negative numbers allowed")
    print("Valid number:", num)
except ValueError as e:
    print("Error:", e)
