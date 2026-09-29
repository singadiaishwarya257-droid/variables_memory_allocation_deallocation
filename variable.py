#variable name->object(identity,type,value)->memory(no longer need)->eligible to reclamation
x= 10
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
is_week=False
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






