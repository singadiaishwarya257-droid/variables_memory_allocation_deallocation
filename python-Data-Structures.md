# Python Data Structures — Interview Notes

## 1. Quick Comparison

| Data Structure | Ordered | Mutable | Duplicates | Indexing | Hashable | Main Use |
|---|---|---|---|---|---|---|
| **List** | Yes | Yes | Yes | Yes | No | Ordered, dynamic data |
| **Tuple** | Yes | No | Yes | Yes | Only if all items are hashable | Fixed data |
| **Set** | No | Yes | No | No | Elements must be hashable | Unique values, membership |
| **Dictionary** | Yes (insertion order) | Yes | Keys unique | By key | Keys must be hashable | Key-value lookup |

---

## 2. List

### Built-in Functions

#### `len()` — Built-in Function
Definition: Returns the number of elements in the list.

```python
numbers = [10, 20, 30]
print(len(numbers))
```

Output:
```text
3
```

#### `sum()` — Built-in Function
Definition: Returns the sum of all numeric elements in the list.

```python
numbers = [10, 20, 30]
print(sum(numbers))
```

Output:
```text
60
```

#### `max()` — Built-in Function
Definition: Returns the largest element in the list.

```python
numbers = [10, 20, 30]
print(max(numbers))
```

Output:
```text
30
```

#### `min()` — Built-in Function
Definition: Returns the smallest element in the list.

```python
numbers = [10, 20, 30]
print(min(numbers))
```

Output:
```text
10
```

#### `sorted()` — Built-in Function
Definition: Returns a new sorted list without changing the original list.

```python
numbers = [30, 10, 20]
print(sorted(numbers))
print(numbers)
```

Output:
```text
[10, 20, 30]
[30, 10, 20]
```

#### `reversed()` — Built-in Function
Definition: Returns an iterator that goes through the list in reverse order.

```python
numbers = [10, 20, 30]
print(list(reversed(numbers)))
```

Output:
```text
[30, 20, 10]
```

### Methods

#### `append()` — List Method
Definition: Adds one element to the end of the list.

```python
numbers = [1, 2]
numbers.append(3)
print(numbers)
```

Output:
```text
[1, 2, 3]
```

#### `extend()` — List Method
Definition: Adds all items from another iterable to the end of the list.

```python
numbers = [1, 2]
numbers.extend([3, 4])
print(numbers)
```

Output:
```text
[1, 2, 3, 4]
```

#### `insert()` — List Method
Definition: Inserts an element at a specific index.

```python
numbers = [10, 20, 30]
numbers.insert(1, 15)
print(numbers)
```

Output:
```text
[10, 15, 20, 30]
```

#### `remove()` — List Method
Definition: Removes the first matching value from the list.

```python
numbers = [10, 20, 30, 20]
numbers.remove(20)
print(numbers)
```

Output:
```text
[10, 30, 20]
```

#### `pop()` — List Method
Definition: Removes and returns the last element of the list.

```python
numbers = [10, 20, 30]
print(numbers.pop())
print(numbers)
```

Output:
```text
30
[10, 20]
```

#### `clear()` — List Method
Definition: Removes all elements from the list.

```python
numbers = [1, 2, 3]
numbers.clear()
print(numbers)
```

Output:
```text
[]
```

#### `index()` — List Method
Definition: Returns the index of the first matching value.

```python
numbers = [10, 20, 30]
print(numbers.index(20))
```

Output:
```text
1
```

#### `count()` — List Method
Definition: Returns how many times a value appears in the list.

```python
numbers = [1, 2, 2, 3]
print(numbers.count(2))
```

Output:
```text
2
```

#### `sort()` — List Method
Definition: Sorts the list in place.

```python
numbers = [30, 10, 20]
numbers.sort()
print(numbers)
```

Output:
```text
[10, 20, 30]
```

#### `reverse()` — List Method
Definition: Reverses the list in place.

```python
numbers = [10, 20, 30]
numbers.reverse()
print(numbers)
```

Output:
```text
[30, 20, 10]
```

#### `copy()` — List Method
Definition: Creates a shallow copy of the list.

```python
numbers = [1, 2, 3]
copy_numbers = numbers.copy()
print(copy_numbers)
```

Output:
```text
[1, 2, 3]
```

### Operations

#### Indexing
Definition: Accesses an element by its position.

```python
numbers = [10, 20, 30]
print(numbers[0])
print(numbers[-1])
```

Output:
```text
10
30
```

#### Slicing
Definition: Extracts a part of the list using start, stop, and step.

```python
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])
print(numbers[::-1])
```

Output:
```text
[20, 30, 40]
[50, 40, 30, 20, 10]
```

#### Concatenation
Definition: Joins two lists together.

```python
a = [1, 2]
b = [3, 4]
print(a + b)
```

Output:
```text
[1, 2, 3, 4]
```

#### Repetition
Definition: Repeats the list elements a specified number of times.

```python
print([1, 2] * 3)
```

Output:
```text
[1, 2, 1, 2, 1, 2]
```

#### Membership
Definition: Checks whether an element exists in the list.

```python
numbers = [10, 20, 30]
print(20 in numbers)
```

Output:
```text
True
```

### List Interview Traps
- **`append()` vs `extend()`**: `append([3, 4])` adds one list item, while `extend([3, 4])` adds the elements `3` and `4`.
- **`remove()` vs `pop()` vs `del`**: `remove()` uses value, `pop()` uses index and returns the removed value, `del` also uses index.
- **`sort()` vs `sorted()`**: `sort()` modifies the original list, `sorted()` returns a new list.

### List Time Complexity
| Operation | Complexity |
|---|---:|
| Index access | O(1) |
| Append | O(1) amortized |
| Search | O(n) |
| Insert/Delete in middle | O(n) |
| sort() | O(n log n) |

---

## 3. Tuple

### Built-in Functions

#### `len()` — Built-in Function
Definition: Returns the number of elements in the tuple.

```python
t = (10, 20, 30)
print(len(t))
```

Output:
```text
3
```

#### `sum()` — Built-in Function
Definition: Returns the sum of numeric values in the tuple.

```python
t = (10, 20, 30)
print(sum(t))
```

Output:
```text
60
```

#### `max()` — Built-in Function
Definition: Returns the maximum element in the tuple.

```python
t = (10, 20, 30)
print(max(t))
```

Output:
```text
30
```

#### `min()` — Built-in Function
Definition: Returns the minimum element in the tuple.

```python
t = (10, 20, 30)
print(min(t))
```

Output:
```text
10
```

### Methods

#### `count()` — Tuple Method
Definition: Counts how many times a value appears in the tuple.

```python
t = (10, 20, 10, 30)
print(t.count(10))
```

Output:
```text
2
```

#### `index()` — Tuple Method
Definition: Returns the first index of a value in the tuple.

```python
t = (10, 20, 30)
print(t.index(20))
```

Output:
```text
1
```

### Operations

#### Indexing
Definition: Accesses a tuple element by position.

```python
t = (10, 20, 30)
print(t[0])
```

Output:
```text
10
```

#### Slicing
Definition: Extracts a range of elements using slices.

```python
t = (10, 20, 30, 40)
print(t[1:3])
```

Output:
```text
(20, 30)
```

#### Concatenation
Definition: Joins two tuples into one tuple.

```python
print((1, 2) + (3, 4))
```

Output:
```text
(1, 2, 3, 4)
```

#### Repetition
Definition: Repeats the tuple elements a number of times.

```python
print((1, 2) * 2)
```

Output:
```text
(1, 2, 1, 2)
```

#### Membership
Definition: Checks whether a value exists in the tuple.

```python
t = (10, 20, 30)
print(20 in t)
```

Output:
```text
True
```

#### Packing and Unpacking
Definition: Stores values in a tuple and extracts them back into variables.

```python
student = ("Aishwarya", 21, "BCA")
name, age, course = student
print(name, age, course)
```

Output:
```text
Aishwarya 21 BCA
```

### Tuple Interview Traps
- **Singleton tuple:** `(10,)` is a tuple, but `(10)` is an integer.
- **Tuple is immutable**: you cannot modify it after creation.
- **Tuple hashability**: a tuple is hashable only if all its elements are hashable.

### Tuple Time Complexity
| Operation | Complexity |
|---|---:|
| Index access | O(1) |
| Search | O(n) |
| Length | O(1) |
| Slicing | O(k) |

---

## 4. Set

### Built-in Functions

#### `len()` — Built-in Function
Definition: Returns the number of elements in the set.

```python
s = {10, 20, 30}
print(len(s))
```

Output:
```text
3
```

#### `min()` — Built-in Function
Definition: Returns the smallest value in the set.

```python
s = {10, 20, 30}
print(min(s))
```

Output:
```text
10
```

#### `max()` — Built-in Function
Definition: Returns the largest value in the set.

```python
s = {10, 20, 30}
print(max(s))
```

Output:
```text
30
```

#### `sorted()` — Built-in Function
Definition: Returns a sorted list from the set.

```python
s = {30, 10, 20}
print(sorted(s))
```

Output:
```text
[10, 20, 30]
```

### Methods

#### `add()` — Set Method
Definition: Adds one element to the set.

```python
s = {1, 2}
s.add(3)
print(s)
```

Output:
```text
{1, 2, 3}
```

#### `update()` — Set Method
Definition: Adds multiple elements to the set.

```python
s = {1, 2}
s.update([3, 4])
print(s)
```

Output:
```text
{1, 2, 3, 4}
```

#### `remove()` — Set Method
Definition: Removes an element and raises an error if it is missing.

```python
s = {1, 2, 3}
s.remove(2)
print(s)
```

Output:
```text
{1, 3}
```

#### `discard()` — Set Method
Definition: Removes an element without raising an error if missing.

```python
s = {1, 2, 3}
s.discard(5)
print(s)
```

Output:
```text
{1, 2, 3}
```

#### `pop()` — Set Method
Definition: Removes and returns an arbitrary element.

```python
s = {10, 20, 30}
print(s.pop())
print(s)
```

Output:
```text
10
{20, 30}
```

#### `clear()` — Set Method
Definition: Removes all elements from the set.

```python
s = {1, 2, 3}
s.clear()
print(s)
```

Output:
```text
set()
```

#### `copy()` — Set Method
Definition: Creates a copy of the set.

```python
s = {1, 2, 3}
copy_s = s.copy()
print(copy_s)
```

Output:
```text
{1, 2, 3}
```

### Operations

#### Membership
Definition: Checks whether a value exists in the set.

```python
s = {10, 20, 30}
print(20 in s)
```

Output:
```text
True
```

#### Union
Definition: Returns all unique elements from both sets.

```python
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)
```

Output:
```text
{1, 2, 3, 4, 5}
```

#### Intersection
Definition: Returns only the common elements.

```python
A = {1, 2, 3}
B = {3, 4, 5}
print(A & B)
```

Output:
```text
{3}
```

#### Difference
Definition: Returns elements present in the first set but not in the second.

```python
A = {1, 2, 3}
B = {3, 4, 5}
print(A - B)
```

Output:
```text
{1, 2}
```

#### Symmetric Difference
Definition: Returns elements that are in either set, but not both.

```python
A = {1, 2, 3}
B = {3, 4, 5}
print(A ^ B)
```

Output:
```text
{1, 2, 4, 5}
```

### Set Interview Traps
- **`{}` is not an empty set**; it creates an empty dictionary.
- **`remove()` vs `discard()`**: `remove()` raises an error if missing, `discard()` does not.
- Sets are **unordered**, so they do not support indexing.

### Set Time Complexity
| Operation | Average Complexity |
|---|---:|
| Add | O(1) |
| Remove | O(1) |
| Membership check | O(1) |
| Union | O(n + m) |
| Intersection | O(min(n, m)) average |

---

## 5. Dictionary

### Built-in Functions

#### `len()` — Built-in Function
Definition: Returns the number of key-value pairs in the dictionary.

```python
student = {"name": "Aishwarya", "age": 21}
print(len(student))
```

Output:
```text
2
```

#### `dict()` — Built-in Function
Definition: Creates a dictionary from keyword arguments or pairs.

```python
student = dict(name="Aishwarya", age=21)
print(student)
```

Output:
```text
{'name': 'Aishwarya', 'age': 21}
```

### Methods

#### `get()` — Dictionary Method
Definition: Returns the value for a key, or a default value if the key does not exist.

```python
student = {"name": "Aishwarya"}
print(student.get("name"))
print(student.get("age", 0))
```

Output:
```text
Aishwarya
0
```

#### `keys()` — Dictionary Method
Definition: Returns all keys in the dictionary.

```python
student = {"name": "Aishwarya", "age": 21}
print(student.keys())
```

Output:
```text
dict_keys(['name', 'age'])
```

#### `values()` — Dictionary Method
Definition: Returns all values in the dictionary.

```python
student = {"name": "Aishwarya", "age": 21}
print(student.values())
```

Output:
```text
dict_values(['Aishwarya', 21])
```

#### `items()` — Dictionary Method
Definition: Returns key-value pairs as tuples.

```python
student = {"name": "Aishwarya", "age": 21}
print(student.items())
```

Output:
```text
dict_items([('name', 'Aishwarya'), ('age', 21)])
```

#### `update()` — Dictionary Method
Definition: Inserts or updates key-value pairs from another dictionary.

```python
student = {"name": "Aishwarya"}
student.update({"age": 21, "city": "Athani"})
print(student)
```

Output:
```text
{'name': 'Aishwarya', 'age': 21, 'city': 'Athani'}
```

#### `pop()` — Dictionary Method
Definition: Removes and returns the value for a key.

```python
student = {"name": "Aishwarya", "age": 21}
print(student.pop("age"))
print(student)
```

Output:
```text
21
{'name': 'Aishwarya'}
```

#### `popitem()` — Dictionary Method
Definition: Removes and returns the last inserted key-value pair.

```python
student = {"name": "Aishwarya", "age": 21}
print(student.popitem())
print(student)
```

Output:
```text
('age', 21)
{'name': 'Aishwarya'}
```

#### `setdefault()` — Dictionary Method
Definition: Returns the value if the key exists, otherwise inserts a default value.

```python
student = {"name": "Aishwarya"}
print(student.setdefault("age", 21))
print(student)
```

Output:
```text
21
{'name': 'Aishwarya', 'age': 21}
```

#### `clear()` — Dictionary Method
Definition: Removes all key-value pairs from the dictionary.

```python
student = {"name": "Aishwarya"}
student.clear()
print(student)
```

Output:
```text
{}
```

### Operations

#### Key Access
Definition: Accesses a value using its key.

```python
student = {"name": "Aishwarya", "age": 21}
print(student["name"])
```

Output:
```text
Aishwarya
```

#### Insertion
Definition: Adds a new key-value pair to the dictionary.

```python
student = {"name": "Aishwarya"}
student["city"] = "Athani"
print(student)
```

Output:
```text
{'name': 'Aishwarya', 'city': 'Athani'}
```

#### Update
Definition: Changes the value of an existing key.

```python
student = {"name": "Aishwarya", "age": 21}
student["age"] = 22
print(student)
```

Output:
```text
{'name': 'Aishwarya', 'age': 22}
```

#### Delete
Definition: Removes an item by key.

```python
d = {"name": "Aishwarya", "age": 21}
del d["age"]
print(d)
```

Output:
```text
{'name': 'Aishwarya'}
```

#### Membership
Definition: Checks whether a key exists in the dictionary.

```python
student = {"name": "Aishwarya", "age": 21}
print("name" in student)
print("Aishwarya" in student)
```

Output:
```text
True
False
```

### Dictionary Interview Traps
- **`dict[key]` vs `dict.get(key)`**: `dict[key]` raises an error if missing, `dict.get(key)` returns `None` or a default value.
- **Membership checks keys, not values**: `"name" in student` checks for key presence, not value presence.
- **Duplicate keys are overwritten**: the last value wins.
- **Lists and sets cannot be dictionary keys** because they are unhashable.

### Dictionary Time Complexity
| Operation | Average Complexity |
|---|---:|
| Lookup | O(1) |
| Insert | O(1) |
| Update | O(1) |
| Delete | O(1) |
| Iteration | O(n) |

---

## 6. Final Interview Notes

### Must-Know Differences
- **List vs Tuple**: list is mutable, tuple is immutable.
- **List vs Set**: list allows duplicates, set does not.
- **Set vs Dictionary**: set stores unique values, dictionary stores key-value pairs.
- **Mutable vs Immutable**: mutable objects can change after creation; immutable ones cannot.
- **Hashable vs Non-hashable**: hashable objects can be used as set/dict keys.
- **`append()` vs `extend()`**: one item vs many items.
- **`remove()` vs `discard()`**: `remove()` raises error, `discard()` does not.
- **`dict[key]` vs `dict.get(key)`**: direct access vs safe access.

### Short Summary
- **List** = ordered + mutable + duplicates allowed
- **Tuple** = ordered + immutable + fixed data
- **Set** = unique + hash-based membership
- **Dictionary** = key-value + fast lookup

### Why lookup is fast
- **List**: search is O(n)
- **Set / Dictionary**: hashing gives average O(1) lookup

### Input → Method → Output Flow
```python
numbers = [10, 20]
numbers.append(30)
print(numbers)
```

Output:
```text
[10, 20, 30]
```

This is the exact pattern interviewers expect: understand the data structure, know the method, and know the result.
