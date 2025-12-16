# DEEP DIVE: Micro-Challenge: The Guard Clause (Short-Circuiting)

# Scenario 1: user is None (This is the critical test case)
user = None

# If we tried to check the access directly, it would crash:
# if user.has_access("admin"):  # <-- This line would raise an AttributeError

print("--- Scenario 1: User is None ---")

# The Guard Clause: Python checks the first condition (A) first.
# if user is not None is False, Python SHORT-CIRCUITS and never executes B.
if user is not None and user.has_access("admin"):
    print("User has admin access and is logged in.")
else:
    print("Access denied or user is not logged in.")
# Output will be: Access denied or user is not logged in.
# The code does NOT
