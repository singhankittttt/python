'''print("Hello World")
print(20+85)

name = "ankit"
age = 21
price = 20.99

print(name, age, price)

print("name is singh")

print("My name is singh")

print(type(name))
print(type(age))
print(type(price))'''

''' keywords in python:
and, else, in, return, as, except, is, True, assert, finally, lambda, try, break, false, nonlocal, with, for, None, while, from, not, yield, global, or, if, pass, import, raise
'''

# Assignment Operator
'''num = 10
num = num + 10
num += 10
num *= 10
num /= 10
print("num :", num)'''

'''name = input("What is your name? ")
print("Hello my name is " + name)

old_age = input("enter your old age : ")
new_age = int(old_age) + 2
print(new_age)'''

'''first = input("enter first number ")
second = input("enter second number ")

sum = int(first) + int(second)
print("the sum is : " + str(sum))'''

'''name = "Tony Stark"
print(name.upper())
# 0 index
print(name.find('S'))

print("hi")
print("my name is singh")'''

'''a = 5
b = 2
print(a >= b)  # relational
print(a ** b)  # power'''

'''Arithmetic Operators(+, -, *, /, %, **)
   Relational/Comparison Operators(==, !=, >, <, <=, <=)
   Assignment Operators(=, +=, -=, *=, /=, %=, **=)
   Logical Operator(not, and, or)'''

# logical operator
'''a = 50
b = 30
print(not False)
print(not True)
print(not (a > b))'''

# AND Operator
'''val1 = True
val2 = False
print("AND operator:", val1 and val2)'''

# OR Operator
'''val1 = True
val2 = False
# print("OR operator:", val1 or val2)
print("OR operator", (a == b) or (a > b))'''

# type conversion(automatically)
'''a = int("2")
b = 4.25

# sum = a + b # 2.0 + 4.25 => 6.25
# print(sum)

# type casting
print(type(a))
print(a + b)'''

# name = input("Enter your name: ")
# print("welcome", name)

# WAP to check if a number entered by the user is odd or even

'''num = int(input("Enter a number: "))
if (num % 2 == 0):
    print("It is a even number")
else:
    print("It is an odd number")'''

# WAP to find the greatest of 3 number entered by the user

'''a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter a third number: "))
d = int(input("enter a fourth number: "))

if (a >= b and a >= c and a >= d):
    print("first number is largest", a)
elif (b >= a and b >= c and b >= d):
    print("second number is largest", b)
elif (c >= a and c >= b and c >= d):
    print("third is largest", c)
else:
    print("fourth is largest", d)'''

# WAP to check if a number is a multiple of 7 or not

'''x = int(input("enter a number: "))

if (x % 5 == 0):
    print("multiple of 5")
else:
    print("not a multiple")'''

# list in python
# list are mutable

'''marks = [94.4, 65.2, 54.9, 87.6]
print(marks)
print(len(marks))
print(marks[0])'''

'''student = ["karan", 95.4, 17, "Delhi"]
print(student[0])
student[0] = "arjun"
print(student)'''

# Strings are immutable
'''str = "hello"
print(str[0])
str[0] = "y"'''

# List Slicing

'''marks = [87, 54, 65, 21, 38]
print(marks[0:4])
print(marks[-3:-1])'''

# List Methods

# list = [2, 1, 9, 8, 7]
# list.append(9)
# list.sort()
# list.sort(reverse=True)
# list.insert(0, 6)
# list.remove(1)
# list.pop(0)
# print(list)

# Tuples in Python
# A built-in data types that lets us create immutable sequences of values.

'''tup = (87, 54, 84, 62, 21)
print(type(tup))
print(tup[1])
tup[0] = 5'''

'''tup = ("ankit")
print(tup)
print(type(tup))'''

# Tuple methods
'''tup = (2, 1, 3, 1)
print(tup.index(3))
print(tup.count(5))'''

# Q.) WAP to ask the user to enter names of their 3 favourite movies & store them in a list.

'''movies = []
movies.append(input("enter 1st movie: "))
movies.append(input("enter 2nd movie: "))
movies.append(input("enter third movie: "))

print(movies)'''

# Q.) WAP to check if a list contains a palindrome of elements.(Hint: use copy() method)

'''list1 = [1, "abc", "abc", 1]
list2 = [1, 2, 3]

copy_list1 = list2.copy()
copy_list1.reverse()

if (copy_list1 == list1):
    print("palindrome")
else:
    print("NOT palindrome")'''

# WAP to count the number of students with the "A" grade in the following tuple.

'''listn = ["C", "D", "A", "A", "B", "B", "A"]

copy_listn = listn.copy()
copy_listn.reverse()

if (copy_listn == listn):
    print("palindrome")
else:
    print("NOT palindrome")

print(listn.count("A"))
listn.sort()
print(listn)'''

# Dictionary in python
# dictionary are mutable(changeable), unordered & don't allow duplicate keys
# "key" : value

'''dict = {
    "name": "ankit",
    "age": 25,
    12.99: 94.4,
    "key": "value",
    "cgpa": 9.6,
    "marks": [98, 97, 95],
    "is_adult": True,
    "subject": ["python", "C", "Java"]
}

dict.update()
print(dict)
print(dict["is_adult"])
print(type(dict))
dict["name"] = "anima"
print(dict)'''

'''null_dict = {}
null_dict["name"] = "singh"
print(null_dict)'''

# Nested dictionaries

'''student = {
    "name": "ankit singh",
    "score": {
        "chem": 98,
        "phy": 99,
        "math": 97
    }
}'''

# print(student)

# nested dictionary

# print(student["score"]["chem"])

# Dictionary methods

# print(len(list(student.keys())))
# print(student.values())
# print(list(student.items()))

# pairs = list(student.items())
# print(pairs[0])

# print(student.get("name"))

# new_dict = {"name": "money singh", "age": 16}
# student.update(new_dict)

# print(student)

# Sets in Python
# each element in the set must be unique & immutable(not change).
# duplicates values are not allowed in sets

'''collection = {1, 2, 2, 2, 3, 4, "hello", "wolrd", 4}
set2 = {1, 2, 2, 2}
# repeated elements stored only once, so it resolved to {1,2}

print(collection)
print(type(collection))
print(len(collection))
null_set = set()
print(type(null_set))'''

# Sets Methods
'''collect = set()
collect.add(1)
collect.add(2)
collect.add("ankit")
collect.add((1, 2, 3))'''

set1 = {1, 2, 3, 4}
set2 = {3, 4, 7, 8}
# collect.add({1, 2, 3})

# collect.remove(1)
# collect.remove(7)
# collect.clear()
# print(len(collect))
# print(collect.pop())
# print(collect.pop())

# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1)
# list are Unhasable type means an alogorithms where we change values of one type to another type
# print(collect)

# Q.) store following word meanings in a python dictionary:
#   table: "a piece of furniture", "list of facts & figures"
#   cat : "a small animal"

'''dic = {
    "table": ["a piece of furniture", "list of facts & figures"],
    "cat": "a small animal"
}

print(dic)'''

# Q.) you are given a list of subjects for students. assume one classroom is required for 1 subject. how many classrooms are needed by all students.
'''subjects = {
    "python", "java", "c++", "python", "javascript", "java",
    "python", "java", "c++", "c"
}

print(len(subjects))'''

# wap to enter marks of 3 subjects from the user and store them in a dictionary. start with an empty dictionary & add one by one. use subject name as key & marks as value

'''marks = {}

x = int(input("enter phy: "))
marks.update({"phy": x})

x = int(input("enter chem: "))
marks.update({"chem": x})

x = int(input("enter math: "))
marks.update({"math": x})

print(marks)'''

# figure out a way to store 9 & 9.0 as seperate values in the set.
# (you can take help of built-in data types)

# values = {9, 9.25, 8, "8.0"}
# print(values)

'''value = {
    ("float", 9.0),
    ("int", 9)
}

print(value)'''

'''n1 = 0
n2 = 1
n3 = 1

if (n3 >= n1 + n2):
    print("it is a fibonacci series")
else:
    print("it is not a fibonacci series")'''

# Fibonacci series

'''nterms = int(input("enter number of terms: "))

n1, n2 = 0, 1
count = 0

if nterms <= 0:
    print("enter a positive ineteger")
elif nterms == 1:
    print("fibonacci sequences upto", nterms, ":")
    print(n1)
else:
    print("fibonacci sequences: ")

    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1'''

# factorial of a given number


'''def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while (n > 1):
            fact *= n
            n -= 1
        return fact


num = 5
print("Factorial of", num, "is", factorial(num))'''


# Loops in Python
# loops are used to repeat instructions.
# iteration - complete of one loop

'''count = 1
while count <= 5:
    print("hello")
    count += 1'''

'''i = 1
while i <= 10:
    print("anky", i)
    i += 1'''

'''i = 1
while i <= 5:
    print(i)
    i += 1

print("loop  ended")'''

'''i = 5
while i >= 1:
    print(i)
    i -= 1'''

# 1.) print numbers from 1 to 100.

'''i = 1
while i <= 100:
    print(i)
    i += 1'''

# 2.) print number from 100 to 1

'''i = 100
while i >= 1:
    print(i)
    i -= 1'''

# 3.) print the multiplication table of a number n.

'''n = int(input("enter number: "))
i = 1
while i <= 10:
    print(17*i)
    i += 1'''

# 4.) print the elements of the following list using a loop:
#     [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
heroes = ["ironman", "thor", "krrish", "batman"]

# traverse(travel in every single items inside a loop or list is called traverse.)
'''indx = 0
while indx < len(nums):
    print(nums[indx])
    indx += 1'''

i = 0
while i < len(heroes):
    print(heroes[i])
    i += 1
