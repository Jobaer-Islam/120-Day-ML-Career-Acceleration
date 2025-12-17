word = "DATA"

for ch in word:
    print(ch)


In Python, anything you can loop over (like strings, lists, or ranges) is called an "Iterable."
When you write for char in word:, Python uses a secret set of rules called the "Iterator Protocol." This protocol makes sure Python knows how to:
Fetch the first letter ('D').
Fetch the next letter ('A', then 'T', then 'A').
Know when to stop (when it runs out of letters).

Why this is important?
This concept is used in:

-Text processing
-Password validation
-Parsing files
-NLP (Natural Language Processing)
