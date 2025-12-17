# Create a list object
x = [1, 2, 3]  

# This doesn't copy the list; it just adds a new name (y) to the same list
y = x          

# Changing 'y' affects 'x' because they point to the same "box" in memory
y.append(4)    

print(f"Variable x: {x}") # [1, 2, 3, 4]
print(f"Variable y: {y}") # [1, 2, 3, 4]

Why it works: In Python, variables are labels, not containers. When you say y = x,
you are telling Python, "Wherever x is looking, I want y to look there too."
