 #variable name->object(identity,type,value)->memory(no longer need)->eligible to reclamat x= 10
name="aishu"
marks=85.5
numbers=[10,20,30]
print(id(name))
print(type(name))
print(name)
print(marks)
print(type(marks))
print(numbers)
print(id(x))
print(type(x))

#boolean
is_strong=True
# is_week=False
print(bool(0))
print(bool(1))
print(bool())
print("")
print("hello ji")

#string
brand = "BMW"
print(brand[0])
print(brand[2])

#list
numbers=[40,50,60,70,40,30]
data=[10,"ashh",55.5,True]
print(data)

#tuple
my_tuple=(10,20,30)

#Sets
speed={100,200,300,500}

#dicts
Cars={
    "brand":"bmw",
    "model":"x5",
    "year":2036
}
print(Cars["brand"])

#mutable object
a=[10,20,30]
b=a
b.append(40)
print(a)

# == and is
a=[10,20]
b=[10,20]
print(a == b)
print(a is b)

#REFERENCE COUNTING
a=[60,70,80]
b=a
del b
print(a)

#del
numbers=[10,20,30]
b=numbers
del numbers
print(b)

# funtions
def welcome(name):
    print(welcome,name)
welcome("Aishu")    
welcome("Ashhh")    
welcome("Aisi") 

# function example
def add(a,b):
    return a+b
result=add(2,3)
print(result)

# defining and calling a function
def greet():
    print("hello")
greet()    

# function without parameters
def welcome():
    print("welcome to the nighan2 labs")
welcome()

# what happens after return
def test():
    return 10
    print("good morning") 
print(test())

# returning multiple values
def calculate(a, b):
    return a + b, a - b, a * b


addition, subtraction, multiplication = calculate(10, 5)
print(addition)       
print(subtraction)    
print(multiplication) 


# Positional arguments
def student(name, age):
    print(name, age)


student("Aishu", 21)

#keyword arguments
def student(name, age):
    print(name, age)


student(age=21, name="Aishu")

# *args
def add(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total
print(add(10, 20))         
print(add(10, 20, 30))     
print(add(1, 2, 3, 4, 5)) 

# **kwargs
def student(**details):
    print(details)
student(name="Aishu", age=21, course="BCA")

#Combining parameters, *args, and **kwargs
def example(a, b=10, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
example(1, 2, 3, 4, course="BCA")

#local scope
def test():
    x = 10
    print(x)


test()

#global scope
x = 10
def test():
    print(x)
test()

#global keyword
count = 0
def increment():
    global count
    count += 1
increment()
print(count) 

#Local scope outside a function
def test():
    x = 10
test()
print(x)

#Functions can call other functions
def add(a, b):
    return a + b
def display_result(): 
    result = add(10, 20)
    print(result)
display_result()

  #parameters
def add(x,y):
    return x+y
add(4,5)
print(add(5,6))


def calculate():
    return 10
calculate()
print("hello")

#function calling another function
def add(a, b):
    return a + b


def display_result():
    result = add(10, 20)
    print(result)


display_result()

#Function calling flow
def multiply(a, b):
    return a * b

result = multiply(5, 4)
print(result)

#Passing a function to another function
def square(x):
    return x * x


def process(function, value):
    return function(value)


print(process(square, 5))  
squre = lambda x:x*x
print(squre(5))

#recursion
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)


countdown(5)

#function documentation
def add(a, b):
    """Return the sum of two numbers."""
    return a + b


print(add.__doc__)

 #type hints
def add(a: int, b: int) -> int:
    return a + b
print(add(5))


#smart electricity bill calculator
def calculate_bill(units):
    if units <= 100:
        amount = units * 2
    elif units <= 200:
        amount = 100 * 2 + (units - 100) * 4
    else:
        amount = 100 * 2 + 100 * 4 + (units - 200) * 6

    return amount + 100


units = int(input("Enter units: "))
bill = calculate_bill(units)
print("Bill:", bill)

