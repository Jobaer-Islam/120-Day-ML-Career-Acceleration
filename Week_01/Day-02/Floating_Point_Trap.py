# DEEP DIVE: Micro-Challenge: The Floating Point Trap

# 1. Demonstrating the problem
print("--- The Trap (The Problem) ---")
result = 0.1 + 0.2
print(f"The actual sum in memory is: {result}")
print(f"Is 0.1 + 0.2 exactly equal to 0.3? {result == 0.3}") 

# 2. The recommended fix using round()
print("\n--- The Fix (Data Science Best Practice) ---")
# Round the comparison to a sufficient number of decimal places (e.g., 10)
print(f"Are the rounded values equal? {round(0.1 + 0.2, 10) == round(0.3, 10)}") 
