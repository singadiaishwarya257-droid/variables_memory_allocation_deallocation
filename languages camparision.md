# JavaScript, Node.js, Python, and Java: A Beginner's Comparison

This guide explains how these technologies use variables, functions, and memory.

**First important difference:** JavaScript is a programming language. **Node.js is a program that runs JavaScript** on a computer or server. JavaScript in a browser and JavaScript in Node.js use the same language rules, but have different built-in tools.

## 1. Declaring variables

A variable is a name your code uses for a value, like a label on a box.

```javascript
let score = 10;       // Can assign a different value later
const name = "Ava";   // Cannot assign a different value to this name
var oldStyle = 5;     // Older style; usually avoid in new code
```

```python
score = 10             # Python creates/binds the name when assigned
```

```java
int score = 10;        // Java says the type is int
String name = "Ava";  // Java says the type is String
```

In Python, uppercase names such as `MAX_SCORE` are a convention for constants, not a rule enforced by the language.

## 2. Static and dynamic typing

**A type tells the program what kind of value it has**, such as a number, text, or list.

- Java is **statically typed**: the type is checked before the program runs. An `int` variable cannot be assigned text.
- JavaScript and Python are **dynamically typed**: a name can refer to different kinds of values at different times. Errors can appear when the code runs.

```python
value = 10
value = "ten"  # Allowed: the name now refers to text
```

```java
int value = 10;
// value = "ten"; // Not allowed: text is not an int
```

Dynamic typing does not mean “no types.” The values still have types; the language just gives names more flexibility.

## 3. Primitive values and objects

- **JavaScript** has simple values called primitives, such as numbers, text, and `true`/`false`. Arrays and objects are objects.
- **Python** treats every value as an object: numbers, text, lists, and functions.
- **Java** has primitive types such as `int` and `boolean`, and object references such as `String`, arrays, and class instances.

Think of a reference as an address or label that lets the program find an object. It is not usually a copy of the whole object.

## 4. What does `b = a` do?

It depends on whether `a` contains a simple value or refers to a changeable object.

```python
a = 10
b = a
b = 20
print(a)  # 10: changing b did not change a
```

With a list, the names can refer to the same list:

```python
a = [1, 2]
b = a
b.append(3)
print(a)  # [1, 2, 3]
```

JavaScript arrays and objects work similarly. In Java, assigning an array or object variable copies its reference, not the array/object. To get an independent object, make a copy; a shallow copy may still share nested objects.

## 5. Mutable and immutable values

- **Immutable** means the value itself cannot be changed after it is created.
- **Mutable** means its contents can be changed.

Examples:
- Strings are immutable in JavaScript, Python, and Java. An operation that appears to change a string creates or assigns another string.
- JavaScript arrays, Python lists, and Java arrays can have their contents changed.
- JavaScript objects and Python dictionaries are usually mutable. Java objects can be designed to be mutable or immutable.

```python
text = "cat"
# text[0] = "b"  # Error: strings are immutable
items = [1, 2]
items.append(3)    # Lists are mutable
```

```javascript
const person = { name: "Ava" };
person.name = "Mia"; // Allowed: const protects the name, not the object's contents
```

## 6. Stack and heap: a simple model

Imagine a function call as a page of temporary notes:

- The **stack** keeps track of active function calls and their local work.
- The **heap** is where many objects that need to live beyond a tiny calculation are stored.

This is a model, not a strict rule like “all variables are on the stack and all objects are on the heap.” A variable is a name in the language; the runtime or compiler decides how to represent it. Some values may be optimized or stored differently.

## 7. What happens when a function runs?

When code calls a function, the program remembers where it came from, provides the arguments, creates the function's local working names, and runs its statements. The function may send a result back with `return`.

```python
def add(a, b):
    result = a + b
    return result

answer = add(2, 3)  # answer becomes 5
```

When `add` finishes, its local names are no longer available outside the function. An object they referred to can stay alive if the function returned it or another part of the program still uses it.

## 8. Functions in the four technologies

- JavaScript and Python functions are **first-class**: they can be stored in variables, passed to another function, and returned from a function.
- Node.js uses JavaScript's function rules.
- Java methods belong to classes or objects. Java lambdas and method references can be passed around using a functional interface, such as `Function` or `Runnable`.

```python
def double(number):
    return number * 2

operation = double
print(operation(4))  # 8
```

## 9. Passing values to functions (important)

In **pass-by-value**, a function receives its own copy of the argument value. For an object, that copied value can be a reference to the same object. So the function can change the shared object's contents, but it cannot replace the caller's variable by assigning a new value to its local parameter.

- Java and JavaScript pass argument values. For an object, the value being copied is a reference.
- Python is often described as **call by sharing**: the parameter is a new local name for the same object.

```python
def change_list(items):
    items.append("new")  # Changes the shared list

values = []
change_list(values)
print(values)  # ['new']
```

```python
def replace_list(items):
    items = ["different"]  # Only changes this local parameter

values = ["original"]
replace_list(values)
print(values)  # ['original']
```

This is why saying “Python passes lists by reference” can be confusing: the function shares the list object, but assigning to its parameter does not replace the caller's variable.

## 10. Closures: a function that remembers

A **closure** is a function that keeps access to a value from the place where it was created.

```python
def make_counter():
    count = 0

    def next_count():
        nonlocal count
        count += 1
        return count

    return next_count

counter = make_counter()
print(counter())  # 1
print(counter())  # 2
```

The outer function has finished, but the returned function still needs `count`, so the runtime keeps that value alive. JavaScript closures work similarly. Java lambdas can capture local variables that are final or effectively final; a captured object's contents may still be mutable.

## 11. Garbage collection

Garbage collection is automatic cleanup for objects the program can no longer reach. The runtime looks for objects that are no longer in use by any active part of the program.

An object becomes **eligible** for collection when no live reference can reach it. Eligible does not mean “deleted right now”; the runtime chooses when to do the cleanup.

- Python's `del name` removes a name/reference. It does not destroy an object if another name still refers to it.
- JavaScript has `delete` for object properties, but it is not a command to immediately free the object. Local variables go away according to scope.
- Java has no general `delete` command for objects. When references disappear, the object can become eligible for collection.

Even when an object is cleaned up, the runtime may keep the freed memory available for reuse instead of immediately returning it to the operating system.

## 12. Garbage collection by runtime

- **V8**, the engine commonly used by browsers and Node.js, uses tracing garbage collection. It starts from live references and finds objects that can still be reached.
- **Node.js** uses V8 for JavaScript objects. Node.js also manages native resources, so not every byte used by a Node process is in the JavaScript heap.
- **CPython**, the common Python implementation, mainly counts references and also has a cycle collector for certain unreachable groups of objects that refer to each other.
- **Java's JVM** uses tracing garbage collectors to find and clean objects that are no longer reachable.

A tracing collector can clean up a cycle if nothing outside the cycle can reach it.

## 13. How memory leaks happen even with garbage collection

A garbage collector cannot remove an object that is still reachable, even if the program no longer needs it. This can cause a memory leak.

Common examples:
- A global variable keeps old data forever.
- A cache or list keeps growing and never removes old entries.
- An event listener is added but never removed.
- A callback or closure accidentally keeps a large object alive.
- A Java static field or long-lived collection keeps references to old objects.

The key idea: **the collector can identify unreachable objects, not guess which reachable objects you have stopped caring about.**

## 14. What runs the program?

- JavaScript runs in an engine. V8 is used by Chrome and commonly by Node.js.
- Node.js includes V8 plus server APIs and support for asynchronous work, including the libuv library.
- Python can run on different implementations. CPython is the most commonly used one.
- Java runs on the JVM (Java Virtual Machine), which loads and runs Java bytecode and manages memory.

JavaScript is the language; Node.js is one environment for running it, much like a browser is another environment.

## 15. Compiling, interpreting, and JIT

“Compiled” and “interpreted” are not opposites that neatly classify every language.

- **JavaScript/V8:** the engine parses and runs the code, and can compile frequently used code to machine instructions while the program runs. This is called JIT compilation.
- **CPython:** Python source is usually turned into bytecode, then CPython runs that bytecode.
- **Java:** `javac` turns Java source into bytecode. The JVM runs it and may JIT-compile frequently used parts to machine code.

So a language may use both compilation and interpretation steps, depending on its runtime.

## 16. Event loops, threads, and task types

- **Node.js** commonly uses an event loop for waiting on network or file operations. This is useful for many I/O tasks. A long CPU-heavy JavaScript task can block the event loop; worker threads or separate processes can help with CPU-heavy work.
- **Python** has `asyncio` for asynchronous I/O, plus threads and processes. In standard CPython builds, the GIL can limit multiple threads from running Python bytecode at the same time, although threads can still be useful while waiting for I/O.
- **Java** provides threads, thread pools, asynchronous APIs, and (in modern JVMs) virtual threads.

**I/O-bound** means mostly waiting for a network, file, or database. **CPU-bound** means mostly doing calculations. The best concurrency approach depends on which kind of work dominates.

## 17. What happens to a web request?

```text
Browser sends HTTP request
  -> server receives it
  -> route function or method runs
  -> code reads variables and creates objects
  -> code may call a database or another API
  -> function returns a result
  -> server sends an HTTP response
```

After the response, temporary data can be collected when nothing references it. If code saves that data in a global variable, cache, or background task, it can stay alive longer.

## 18. Which language is fastest?

There is no single answer. Speed depends on what the program does:

- Calculations may depend on the algorithm, runtime, and optimized libraries.
- Web requests often spend more time waiting for a database or network than running language code.
- Memory use and garbage-collection pauses can affect response time.
- The number of users and the server design also matter.

Measure the actual program: its response time, throughput, CPU use, and memory use. Do not choose only from a general “fastest language” ranking.

## 19. How long do variables and objects live?

- A local variable is normally usable only while its function is running.
- An object can stay alive longer than a local variable if something else still refers to it.
- When no live reference can reach an object, it becomes eligible for cleanup.
- The exact time memory is cleaned or returned to the operating system depends on the runtime.

**Scope** answers “where can I use this name?” **Reachability** answers “can the program still get to this object?” They are related, but not the same.

## 20. What does `result = a + b` do?

The simple idea is: get the values of `a` and `b`, add them according to the language's rules, then make `result` refer to or contain the answer.

### Python

```python
result = a + b
```

Python checks the objects' types to decide what `+` means. It can add numbers or join strings. Unsupported combinations can raise `TypeError`.

### JavaScript

```javascript
const result = a + b;
```

JavaScript can add numbers or join strings. The `+` operator may convert values depending on their types. `const` means the name `result` cannot be reassigned.

### Java

```java
int result = a + b;
```

Java uses the declared types of `a` and `b`. Here, it adds integers and stores the answer in an `int`. A Java `int` has a fixed 32-bit range, so very large results can overflow.

The computer may optimize this work, so this explanation describes what the line means, not the exact machine instructions used.

## Quick summary

- Python and JavaScript let names refer to different types of values over time; Java declarations specify types.
- Assigning an object to another name usually shares the object rather than copying it.
- Changing a shared list or object can be seen through multiple names.
- Functions have local work, but returned or captured objects can outlive a function call.
- Garbage collection cleans unreachable objects, not every object that is merely unused.
- Node.js is a JavaScript runtime, not a separate language.
