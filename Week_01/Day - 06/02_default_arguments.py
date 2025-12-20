"""
Concept: Default Arguments
Default values are used if no argument is provided.
"""

def connect(port=3306):
    print(f"Connecting to {port}")

connect()        # uses default
connect(5432)    # overrides default
