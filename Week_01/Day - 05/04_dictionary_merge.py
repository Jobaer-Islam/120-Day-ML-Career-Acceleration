"""
Concept: Dictionary Merging
User preferences override default settings.
"""

defaults = {
    "theme": "light",
    "audio": "on",
    "language": "en"
}

user_pref = {
    "theme": "dark"
}

# Method 1: update()
merged_settings = defaults.copy()
merged_settings.update(user_pref)

print("Merged using update():", merged_settings)

# Method 2: | operator (Python 3.9+)
merged_pipe = defaults | user_pref
print("Merged using | operator:", merged_pipe)
