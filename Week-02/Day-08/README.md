
#  What is Time Complexity? (Big Picture)

**Time Complexity** describes **how fast or slow a program grows** when input size increases.

* It does **NOT** measure seconds.
* It measures **number of operations**.
* Written using **Big-O notation**:
  `O(1), O(N), O(N²), O(N log N)`

Think of it as:

> “If data becomes 10× bigger, how much slower will my code get?”

---

#  Hint 8.1 — Linear Scan **O(N)**

###  Definition

A **linear scan** checks elements **one by one** until it finds the target.

###  Why O(N)?

Worst case → item is last or missing → checks **all N items**.

---

###  Example (Python)

```python
def contains(lst, target):
    for item in lst:
        if item == target:
            return True
    return False

data = list(range(10_000))
print(contains(data, -5))
```

###  Explanation

* CPU starts at index 0
* Moves step by step
* No shortcut

---

#  Hint 8.2 — Hash Lookup **O(1)**

###  Definition

A **set/dictionary** uses a **hash function** to jump directly to memory.

###  Why O(1)?

* No scanning
* One hash calculation
* One memory access

---

###  Example

```python
data = set(range(10_000))
print(-5 in data)
```

###  Explanation

* Python computes `hash(-5)`
* Jumps directly to bucket
* Same speed for 10 or 10 million items

---

#  Hint 8.3 — The Insertion Trap **O(N)**

###  Definition

Inserting at the **start of a list** forces Python to **shift all elements**.

---

###  Example

```python
lst = list(range(10_000))
lst.insert(0, -1)
```

###  Why slow?

Lists are **contiguous memory**.
Python must move every element **one position right**.

 **append() is O(1)**
 **insert(0, x) is O(N)**

---

#  Hint 8.4 — Queue Bottleneck **O(N)**

###  Definition

Using `list.pop(0)` removes the first element → causes shifting.

---

###  Bad Example

```python
queue = list(range(10_000))
queue.pop(0)
```

###  Correct Way

```python
from collections import deque

queue = deque(range(10_000))
queue.popleft()
```

###  Rule

* `list` ❌ bad for queues
* `deque` ✅ designed for FIFO

---

#  Hint 8.5 — String Builder Trap **O(N²)**

###  Definition

Strings are **immutable** → cannot change in place.

---

###  Bad Example

```python
s = ""
for _ in range(10_000):
    s += "a"
```

###  Why O(N²)?

Each `+=`:

1. Creates new string
2. Copies old content
3. Adds one char

Total work = 1 + 2 + 3 + … + N

---

###  Correct Way

```python
chars = []
for _ in range(10_000):
    chars.append("a")

s = "".join(chars)
```

---

#  Hint 8.6 — Length Trick **O(1)**

###  Definition

`len()` does **not count elements**.

---

###  Example

```python
lst = list(range(1_000_000))
print(len(lst))
```

###  Why O(1)?

Python stores length in metadata (`ob_size`).
`len()` just reads a number.

---

#  Hint 8.7 — Nested Loop **O(N²)**

###  Definition

Two loops → each item compares with every other item.

---

###  Example

```python
list_a = range(1000)
list_b = range(1000)

matches = []
for a in list_a:
    for b in list_b:
        if a == b:
            matches.append(a)
```

###  Danger

10,000 × 10,000 = **100 million operations**

 **Most common cause of slow servers**

---

#  Hint 8.8 — Sorting Cost **O(N log N)**

###  Definition

Python uses **Timsort** (hybrid of merge + insertion sort).

---

###  Example

```python
import random

data = [random.randint(1, 10000) for _ in range(10000)]
sorted_data = sorted(data)
```

###  Key Idea

* Faster than O(N²)
* Slower than O(N)
* **Never sort inside loops**

---

#  Hint 8.9 — Dictionary Creation **O(N)**

###  Definition

Building a dictionary requires **hashing every element once**.

---

###  Example

```python
data = list(range(10_000))
d = {}

for item in data:
    d[item] = True
```

###  Important Distinction

| Operation   | Complexity |
| ----------- | ---------- |
| Build dict  | O(N)       |
| Search dict | O(1)       |

---

#  Hint 8.10 — Slice Copy **O(k)**

###  Definition

List slicing creates a **new list** (shallow copy).

---

###  Example

```python
data = list(range(100_000))
sub = data[:5000]
```

###  Why O(k)?

* Allocates new memory
* Copies `k` references
* Cost depends on slice size

---

#  Final Mental Model (Very Important)

| Operation        | Big-O       | Performance Impact |
| ---------------- | ----------- | ------------------ |
| Hash lookup      | O(1)        | Very fast          |
| Append           | O(1)        | Very fast          |
| len()            | O(1)        | Very fast          |
| Linear scan      | O(N)        | Slows as data grows|
| Insert at start  | O(N)        | Slow               |
| pop(0)           | O(N)        | Slow               |
| Sorting          | O(N log N)  | Moderate cost      |
| Nested loops     | O(N²)       | Very slow          |


---


