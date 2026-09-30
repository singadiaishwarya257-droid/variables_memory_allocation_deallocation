# Python Functions

## 1. Why use functions?

Without a function, repeated work can mean writing the same code many times:

```python
print("aishu")
print("aishi")
print("aishiii")
```

A function lets us reuse that behavior with different values:

```python
def welcome(name):
    print("Welcome", name)


welcome("aishu")
welcome("ashaa")
welcome("ashwini")
```

Functions help with:
- Code reuse
- Less repetition
- Better organization
- Easier maintenance
- Easier testing

## 2. What is a function?

A function is a reusable block of code that performs a specific task.

```python
def add(a, b):
    return a + b


result = add(2, 3)
print(result)  # 5
```

## 3. Defining vs. calling a function

Defining a function gives it a name and body. It does not run the body:

```python
def greet():
    print("Hi!")
```

Calling the function runs its body:

```python
greet()
```

## 4. Function without parameters

A function can run a task without receiving any input:

```python
def welcome():
    print("Welcome to Nighan2 Labs")


welcome()
```

## 5. Function with a parameter

A parameter is a name in the function definition. An argument is the value passed when calling the function.

```python
def welcome(name):
    print("Welcome", name)


welcome("Aisi")
```

Here, `name` is the parameter and `"Aisi"` is the argument.

## 6. Multiple parameters

A function can receive more than one parameter:

```python
def add(a, b):
    print(a + b)


add(10, 20)
```

## 7. `print()` vs. `return`

`print()` displays a value. `return` sends a value back to the caller so the program can use it.

```python
def add(a, b):
    return a + b


result = add(10, 20)
print(result)  # 30
```

## 8. What happens after `return`?

`return` immediately ends that function call. Any statements after it in the same function do not run.

```python
def test():
    return 10
    print("This will not run")


print(test())
```

## 9. Returning multiple values

Python lets a function return multiple values. They are returned together as a tuple and can be unpacked into separate variables.

```python
def calculate(a, b):
    return a + b, a - b, a * b


addition, subtraction, multiplication = calculate(10, 5)
print(addition)       # 15
print(subtraction)    # 5
print(multiplication) # 50
```

## 10. Default parameters

A default parameter value is used when the caller does not provide an argument for that parameter.

```python
def greet(name="Aishu"):
    print("Hello", name)


greet()          # Hello Aishu
greet("Ashwini") # Hello Ashwini
```

Defaults are useful when a value is commonly the same, but callers should still be able to provide another value.

## 11. Positional arguments

Positional arguments are matched to parameters by their order:

```python
def student(name, age):
    print(name, age)


student("Aishu", 21)
```

## 12. Keyword arguments

Keyword arguments identify parameters by name, so their order can vary:

```python
def student(name, age):
    print(name, age)


student(age=21, name="Aishu")
```

## 13. Positional and keyword arguments together

You can provide some arguments positionally and others by keyword. Positional arguments must come before keyword arguments.

```python
def student(name, age, course):
    print(name, age, course)


student("Aishu", age=21, course="BCA")
```

This is invalid because a positional argument follows a keyword argument:

```python
# SyntaxError:
# student(name="Aishu", 21, course="BCA")
```

## 14. `*args`

Use `*args` when a function should accept a variable number of positional arguments. Inside the function, `args` is a tuple.

```python
def add(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print(add(10, 20))         # 30
print(add(10, 20, 30))     # 60
print(add(1, 2, 3, 4, 5))  # 15
```

The name `args` is a convention; the `*` is what collects the positional arguments.

## 15. `**kwargs`

Use `**kwargs` when a function should accept a variable number of keyword arguments. Inside the function, `kwargs` is a dictionary.

```python
def student(**details):
    print(details)


student(name="Aishu", age=21, course="BCA")
```

## 16. Combining parameters, `*args`, and `**kwargs`

A function can accept regular parameters, extra positional arguments, and extra keyword arguments:

```python
def example(a, b=10, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


example(1, 2, 3, 4, course="BCA")
```

The usual order is required parameters, default parameters, `*args`, and then `**kwargs`.

## 17. Local and global scope

A local variable is created inside a function and is available there:

```python
def test():
    x = 10
    print(x)


test()
```

A function can read a global variable defined outside it:

```python
x = 100


def test():
    print(x)


test()  # 100
```

## 18. The `global` keyword

Use `global` to assign to a module-level variable from inside a function:

```python
count = 0


def increment():
    global count
    count += 1


increment()
print(count)  # 1
```

Avoid global state when possible. Parameters and return values usually make functions easier to reuse and test.

## 19. Local scope outside a function

A local variable cannot be accessed outside the function where it was created. The following raises `NameError` when `print(x)` runs:

```python
def test():
    x = 10


test()
print(x)
```

## 20. Functions can call other functions

One function can call another to divide work into smaller tasks:

```python
def add(a, b):
    return a + b


def display_result():
    result = add(10, 20)
    print(result)


display_result()
```

A larger program might follow a flow like:

```text
main() -> validate() -> calculate() -> save() -> display()
```
