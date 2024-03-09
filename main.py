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

import os
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

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# heroes = ["ironman", "thor", "krrish", "batman"]

# traverse(travel in every single items inside a loop or list is called traverse.)
'''indx = 0
while indx < len(nums):
    print(nums[indx])
    indx += 1

i = 0
while i < len(heroes):
    print(heroes[i])
    i += 1'''

# 5.) search for a number x in this tuple using loop:
# [1, 4, 9, 25, 36, 49, 64, 81, 100]

'''nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)

x = 36

i = 0  # initialization
while i < len(nums):
    if (nums[i] == x):
        print("FOUND at idx", i)
        break
    else:
        print("finding...")
   #  print(nums[i])
    i += 1
print("end of loop")'''

#  Break & Continue
# Break - used to terminate the loop when encountered.

'''i = 1
while i <= 5:
    print(i)
    if (i == 3):
        break
    i += 1

print("end of loop")'''

# Continue - terminates execution in the current iteration & continues execution of the loop with the next iteration.

'''i = 0
while i <= 10:
    if (i%2 != 0):
        i += 1
        continue  # skip
    print(i)
    i += 1

print("hello world")'''

# for loops are used for sequential traversal. for traversing list, string, tuples etc.

'''nums = [1, 2, 3, 4, 5]
veggies = ["potato", "brinjal", "ladyfinger", "cucumber"]

# for val in nums:
#   print(val)

for val in veggies:
    print(val)
else:
    print("END")'''

'''tup = (1, 2, 3, 4, 5)

for num in tup:
    print(num)'''

'''str = "ankypanky"

for char in str:
    if (char == 'y'):
        print("y found")
        break
    print(char)
else:
    print("end")'''

# using for loop
# print the elements of the following list using a loop:
# [1,4,9,16,25,36,49,64,81,100]

'''list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for num in list:
    print(num)'''

# search for a number x in this tuple using loop(this is also called linear search):
# [1,4,9,16,25,36,49,64,81,100]

'''nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = 9

idx = 0
for el in nums:
    if (el == x):
        print("number found at idx", idx)
        break
    idx += 1'''

# Range()
# range function returns a sequences of numbers, starting from 0 by default, and increments by 1(by default), and stops before a specified number.
# range(start?, stop, step?)

# print(range(5))
'''seq = range(10)
for i in seq:
    print(i)'''

# for i in range(10):  # range(stop)
#   print(i)

# for i in range(100, 0, -1):  # range(start, stop)
#    print(i)

# for i in range(1, 100, 2):  # range(start, stop, step)
#    print(i)

# print(seq[0])
# print(seq[1])
# print(seq[2])
# print(seq[3])

'''n = int(input("enter a number: "))

for i in range(1, 11):
    print(n * i)'''

# Pass statement
# pass is a null statement that does nothing. it is used as a placeholder for future code.

'''for i in range(10):
    pass

if i > 5:
    pass

print("some useful work")'''

# Q.) wap to find the sum of a first n natural numbers. (using while)

'''n = 7
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("total sum = ", sum)'''

# for i in range(n+1):
#    print(i)
#    sum += 1


# wap to find the factorial of first n numbers.(using for)

'''n = 5
fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1

for i in range(1, n+1):
    fact *= i

print("factorial =", fact)'''

# for i in range(n):
# print(n * n-1)

# Functions & Recursions

# Functions in python
# Block of statements that perform a specific task.
'''a = 5
b = 10

sum = a + b
print(sum)'''


'''def sum(a, b):
    s = a + b
    return s


print(sum(2, 98))'''


'''def calc_sum(a, b):
    sum = a + b
    print(sum)
    return sum


calc_sum(5, 10)

# more lines of code

calc_sum(2, 10)

# more lines of code
calc_sum(12, 17)'''

# function definition


# def calc_sum(a, b):  # parameters
#    return a + b


# sum = calc_sum(1, 2)  # function call; arguments
# print(sum)


'''def print_hello():
    print("hello")
    return "hello"


output  = print_hello()
print(output)'''

# average of 3 numbers


'''def cal_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg


cal_avg(8, 7, 5)'''

# functions in python
# built in functions

# print("meranaam", end="$")
# len()
# type()
# range()

# Default Parameters
# assigning a default value to parameter, which is used when no argument is passed.

'''def cal_prod(a=1, b=1):
    print(a * b)
    return a * b


cal_prod()'''

# Q.) waf to print the length of a list. (list is the parameter)

'''cities = ["delhi", "gurgaon", "noida", "bengaluru", "mumbai", "chennai"]
heroes = ["thor", "ironman", "captain america", "vampire"]


def print_len(list):
    print(len(list))


print_len(cities)
print_len(heroes)'''

# Q.) waf to print the elements of a list in a single line. (list is the parameter)

'''cities = ["delhi", "gurgaon", "noida", "bengaluru", "mumbai", "chennai"]
heroes = ["thor", "ironman", "captain america", "vampire"]


def print_len(list):
    print(len(list))


def print_list(list):
    for item in list:
        print(item, end=" ")


print_list(cities)'''

# Q.) WAF to find the factorial of n. (n is the parameter)

'''n = 5


def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)


cal_fact(6)'''

# Q.) WAf to convert USD to INR.


'''def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")


converter(72)'''

# Q.) waf to take value as input and return the value as string odd and even.

# Recursion
# when a function calls itself repeatedly

# prints n to 1 backwards


'''def show(n):
    if (n == 0):
        return
    print(n)
    show(n-1)


show(8)'''

# return n!

'''def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)
    
print(fact(4))'''

# Q.) write a recursive function to calculate the sum of first n natural numbers.


'''def calc_sum(n):
    if (n == 0):
        return 0
    return calc_sum(n-1) + n


sum = calc_sum(10)
print(sum)'''

# Q.) write a recursive function to print all elements in a list.
# Hint: use list & index as parameters.


'''def print_list(list, idx=0):
    if (idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)


fruits = ["mango", "apple", "banana", "litchi"]

print_list(fruits)'''

# Files I/O in Python
# python can be used to perform opeartions on a file.(read & write data)

# Types of all files

# 1. Text Files: ,txt, .docx, .log etc
# 2. Binary files: .mp4, .mov, .png, .jpeg etc.

# 'r' - open for reading (default)
# 'w' - open for writing, truncating the file first
# 'x' - create a new file and open it for writing
# 'a' - open for writing, appending to the end of the file if it exists
# 'b' - binary mode
# 't' - text mode (default)
# '+' - open a disk for updating (reading and writing)

# f.readline() - read only single line at a time

'''f = open("singh.txt", "rt")
# data = f.read()
line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

# print(type(line1))
f.close()'''

# writing to a file

# f = open("singh.txt", "a")

# f.write("\nafter that c")
# f.close()

# f = open("main.txt", "a")
# f.close()

# f = open("singh.txt", "a+")
# f.write("abc")
# print(f.read())
# f.write("abc")
# f.close()

# with Syntax:

# with open("singh.txt", "r") as f:
#    data = f.read()
#    print(data)

# with open("singh.txt", "w") as f:
#    f.write("new data")

# Deleting a File
# using the os module
# Module (like a code library) is a file written by another programmer that generally has a functions we can use.

# import os
# os.remove("singh.txt")

# Q.) Create a new file "practice.txt using python. Add the follwing data in it: "

# with open("practice.txt", "w") as f:
#    f.write("Hi everyone \nwe are learning File I/O \nusing java. \ni like programming in Java")

# Q.) waf that replace all occurences of "java" with "python" in the above file.

'''with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("java", "Python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)'''

# Q.) Search if the word "learning" exists in the file or not.

'''word = "xlearning"
with open("practice.txt", "r") as f:
    data = f.read()
    if (data.find(word) != -1):
        print("Found")
    else:
        print("Not Found")'''

# Q.) waf to find in which line of the file does the word "learning" occur first.
# Print-1 if word not found


'''def check_for_line():
    word = "pyq"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if (word in data):
                print(line_no)
            line_no += 1

    return -1


print(check_for_line())'''

# Q.) from a file containing numbers seperated by comma, print the count of even numbers.

'''count = 0
with open("practice.txt", "r") as f:
    data = f.read()
    print(data)

num = ""
for i in range(len(data)):
    if (data[i] == ","):
        print(int(num))
        num = ""
    else:
        num += data[i]

nums = data.split(",")
for val in nums:
    if (int(val) % 2 == 0):
        count += 1

print(count)'''

# OOP in Python
# To map with real world scenarios, we started using objects in code.
# This is called object oriented programming.

# Class & Object in Python
# Class is a blueprint for creating objects.

# creating class


# class Student:
#    name = "Ankit Singh"

# creating object (instance of class)


# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)

# class Car:
#    color = "blue"
#    brand = "mercedes"


# car1 = Car()
# print(car1.color)
# print(car1.brand)

#  __init__ Function
# Constructor - All classes have a function called __init__(), which is always executed when the is being initiated.

'''class Student:

    # default constructors
    def __init__(self):
        pass

    # parameterized constructors
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database..")


s1 = Student("Karan", 97)
print(s1.name, s1.marks)

s2 = Student("Arjun", 88)
print(s2.name, s2.marks)'''
# print(s1.name)

# s2 = Student()
# print(s2.name)

# Class & instances Attributes
# Class.attr
# obj.attr


'''class Student:
    college_name = "DSU"
    name = "anonymous"  # class attr

    def __init__(self, name, marks):
        self.name = name  # obj attr > class attr
        self.marks = marks
        print("adding new student in Database..")


s1 = Student("Arjun", 91)
print(s1.name, s1.marks)

print(Student.college_name)'''

# Methods
# methods are function that belong to objects

# creating class


'''class Student:
    def __init__(self, fullname):
        self.name = fullname

    def hello(self):
        print("hello", self.name)

    def welcome(self):
        print("welcome student")

# creating object

s1 = Student("karan")
s1.hello()
s1.welcome()'''

# Q.) Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.


'''class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is", sum / 3)


s1 = Student("tony stark", [98, 97, 99])
s1.get_avg()

s1.name = "ironman"
s1.get_avg()'''

# Static Methods
# Methods that don't use the self parameter(work at class level)


'''class Student:
    @staticmethod  # decorator -  that we want to create static method
    def college():
        print("ABC College")


s1 = Student()
s1.college()'''

# 'Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.

# Abstraction
# hiding the implementation details of a class and only showing the essential features to the user.

# Encapsulation
# wrapping data and functions into a single unit(object).


'''class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started..")


car1 = Car()
car1.start()'''

# Encapsulation
# wrapping data and function into a single unit(object).

# Q.) create Account class with 2 attribute - balance & account no.
# Q.) Create methods for debit, credit & printing the balance.


'''class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    # debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance = ", self.get_balance())

    # credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(10000, 123456)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
# print(acc1.balance)
# print(acc1.account_no)'''

# del keyword
# used to delete object properties or object itself.


'''class Student:
    def __init__(self, name):
        self.name = name


s1 = Student("ankit")
print(s1.name)
del s1.name
print(s1.name)'''

# private(like) attributes & methods
# Conceptual implementations in python
# private attributes & methods are meant to be used only within the class and are not accessible from outside the class.


class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.acc_pass = acc_pass


acc1 = Account("12345", "abcdef")

print(acc1.acc_no)
print(acc1.acc_pass)
