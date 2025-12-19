"""
Concept: Frequency Counter
Counts how many times each character appears.
"""

word = "banana"
frequency = {}

for ch in word:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print("Frequency count:", frequency)
