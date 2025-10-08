# this is a single line comment 
print("WELCOME  TO COMP417 - NEURAL NETWORKS COURSE!")

# Fstring and dynamically typed variables.
x = 5
print(f"the type of x is {type(x)}")

# python does not have a 'char' class type.
c = "s"
print(f"the type of c is {type(c)}")

# retreving data from the user using the input() function
name = input("what is your name?")
print(f"welcome, {name} to the Comp417 course")

# type casting
# the input() function returns a class str value only.
age = int(input("What is your age? "))
print(f"you are {age} years old, the type of age is {type(age)}")

# conditional rendering in python
x = 40
if x > 60:
    print(f"x is {x} the student is passed")
else:
    print(f"the student faild, x is {x}")

# loops in python
for i in range(1,21,1):
    print(f"i = {i}")

# looping through itrabl objects in python.
s = "Abanoub Refaat"
for c in s:
    print(c)

# functions in python
def fun(param_1, param_2, param_3="did not specify a param_3"):
    print(f"this is a python function, with param_1 {param_1}, param_2 {param_2}, and param_3 {param_3}")

fun(1, 2)

# returning more than one value as a tuble
def sum(x, y, z):
    return (x + y), (y + z), (x + y)

print(sum(1, 2, 3))
a, b, c = sum(3, 2, 1)
print(f"a = {a}, b = {b}, and c = {c}")

# swaping elements in python
a, b = b, a
print(f"a = {a}, and b = {b}")

# data sturctures in python
# 1. lists
new_list = [1, "2", True]
print(len(new_list))
print(new_list[0:])

# reverseing the list using list slicing
print(new_list[-1::-1])

# 2. tubles
new_tuble = (1, 2, 3, 4)
new_tuble.append(5)
new_tuble.remove(2)
print(new_tuble[2])

# 3. Dictionaries
new_dec = {1: "one", 2: "two", 3: "three", "four":4}

for key, value in new_dec:
    print(f"key = {key}, value = {value}")

print(new_dec.values())
print(new_dec.keys())

# pythonic features

list = []
for i in range(11):
    if i % 2 == 0:
        list.append(i)
print(list)

# list comprehension feature
pythonic_list = [x for x in range(10) if x % 2 == 0]
print(pythonic_list)

# dictunary comprehension
dic = {x:x*2 for x in range(10) if x % 2 == 0}
print(dic)