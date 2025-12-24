"""
O(1) Hash Lookup
Direct memory jump using hash table.
"""

data = set(range(10_000))
target = -5

print("Found:", target in data)
