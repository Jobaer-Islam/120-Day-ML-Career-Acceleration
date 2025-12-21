"""
Concept: Exception Bubbling
If an error is not caught, it bubbles up and crashes the program.
"""

def divide(a, b):
    return a / b

def main():
    result = divide(10, 0)  # ZeroDivisionError
    print(result)

main()
