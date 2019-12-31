# if CONDITIONAL STATEMENT
# We use these statement in order to execute block of codes if certain condition(s) is/are met. If those condition are
# not justified then those statement will not be executed. Simple if block is as below
#
# if(condition_is_true):
#     do task 1
#     do task 2
#
# Notice that 1st we have tested a condition and then wrote couple of statements. It is really important to focus on
# indentation. Unlike other languages which uses curly braces {} to group together set of statements that belong to a
# group, Python uses indentation to group together set of statement. If 'do task 2' is not properly indented then it
# will not be part of if block and will e executed irrespective of the condition in if block is true or false. Let's
# take some examples

print("if CONDITIONAL STATEMENT")
# Let's input 1 number from users and check if it number or character

print("\nExample 1")
num1 = input("Please enter a number: ")
if num1.isnumeric():
    print("You have entered a valid number")
if not num1.isnumeric():
    print("Please enter a valid number")

print("\nExample 2")
num1 = input("Please enter a number: ")
if num1.isnumeric():
    print("You have entered a valid number")
    print(f"You entered {num1}")
if not num1.isnumeric():
    print("Please enter a valid number")
print(f"You entered {num1}")

print("\nExample 3")
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # changing string to integer by using int() function
if age < 18:
    print(f"{name}, this movie is for 18+ only. Please come back after {18 - age} years")

# if-else CONDITIONAL STATEMENT
# if-else Statement are upgrade of if statements as it also gives us flexibility to
# execute some statement if condition is met unlike if statement where we only have option of executing some codes
# only when condition is met. Syntax for these statements are as below
# if(condition_is_true):
#     do task 1
# else:
#     do task 2

print("\nif-else CONDITIONAL STATEMENT")
print("\nExample 4")
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
if age >= 18:
    print(f"Welcome {name}. You can cast your vote.")
else:
    print(f"Sorry {name}. Only 18+ are allowed to vote.")
    print(f"Please com back after {18 - age} years")

print("\nExample 5 (Remastering example 1 using else block")
num1 = input("Please enter a number: ")
if num1.isnumeric():
    print("You have entered a valid number")
else:
    print("Please enter a valid number")

# elIf CONDITIONAL STATEMENT
# Similar to if-else Statements, ifEl statements allows us to test multiple conditions if one condition is not met
# Syntax for these statements are as below
# if(condition_is_true):
#     do task 1
# elif(another_condition_is_true):
#     do task 3
# else:
#     do task 4

print("\nelif CONDITIONAL STATEMENT")
print("\n Example 6")
enteredChar = input("Please enter any character: ")
if enteredChar.isnumeric():
    print(f"You entered '{enteredChar}', which is a number")
elif enteredChar.isalpha():
    print(f"You entered '{enteredChar}', which is an alphabet")
else:
    print(f"You entered '{enteredChar}'. Please entered alpha/numeric character only.")

print("\nExample 7 (Simple Calculator)")
num1 = int(input("Please enter 1st number: "))
num2 = int(input("Please enter 2nd number: "))
ops = input("Press + for addition\nPress - for subtraction \nPress * for multiplication\n press / for division\n")
if ops in ['+', '-', '*', '/']:
    if ops == '+':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif ops == '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif ops == '*':
        print(f"{num1} * {num2} = {num1 * num2}")
    else:
        if num2 == 0:
            print("We cant divide by 0")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("you have not chosen correct operator.")

# FOR LOOPS
# for loop in python is more like iterating through values in a sequence.
print("\nFOR LOOPS")

# Simple For loop
for i in range(1, 10):
    print(i, end=", ")

print()

# using for loop to print even number using steps
for i in range(0, 20, 2):
    print(i, end=", ")

print()

# using for loop to print odd numbers
for i in range(1, 20, 2):
    print(i, end=", ")

print()

# print odd number using if block inside for loop
for i in range(0, 20):
    if i % 2 != 0:
        print(i, end=", ")

print()

# iterating through string using for loop
name = "Siddhant Shah"
capChar = 0
lowChar = 0
for char in name:
    if char != " ":
        if char.isupper():
            print(f"{char} is in upper case")
            capChar += 1
        else:
            print(f"{char} is in lower case")
            lowChar += 1
print(f"Total upper case letter: {capChar} and lower case letter: {lowChar}")

print()

number = "1,234,567,890"
newNumber = ""
# for char in number:
#     if char in "012346789":
#         newNumber += char
# print(f"Old Number:{number}\nNew Number: {newNumber}")
for index in range(0, len(number)):
    if number[index] in "0123456789":
        newNumber += number[index]
print(f"Old Number:{number}\nNew Number: {newNumber}")

counter = 0
numberWithPeriod = ""
for i in range(0, len(number.replace(",", ""))):
    counter += 1
    index = len(number.replace(",", "")) - i-1
    numberWithPeriod += number.replace(",", "")[index]
    if counter % 3 == 0:
        numberWithPeriod += "."
print(f"Number with Period: {numberWithPeriod[::-1]}")

print()
# Example of for Loop iterating through each element of list
itCity = ["Bangalore", "Pune", "Hyderabad", "Delhi"]
for city in itCity:
    print(f"{city} is an IT city in India")

print()

# Printing table of 2
number = input("Please enter a number(0-20 whose table is required: ")
for counter in range(1, 16):
    print(f"{number} times {counter:>2} is {int(number)*counter:>3}")

print()

# Continue in For Loop
# this keyword is used to skip the current iteration of for loop and execute the next iteration
print("CONTINUE\n")
shoppingList = ["Milk", "Bread", "Butter", "Meat", "Rice", "Sugar"]
newShoppingList = []
for item in shoppingList:
    if item == "Meat":
        continue
    newShoppingList.append(item)
for item in newShoppingList:
    print(item)

print()

# Break in For Loop
# this keyword is used to break the execution of for loop and start executing statement followed by for loop
print("Break\n")
shoppingList = ["Milk", "Bread", "Butter", "Meat", "Rice", "Sugar"]
newShoppingList = []
for item in shoppingList:
    if item == "Meat":
        break
    newShoppingList.append(item)
for item in newShoppingList:
    print(item)

print()

# CHALLENGE
print("CHALLANGE\n")
# Create a program that takes an IP address entered at the keyboard
# and prints out the number of segments it contains, and the length of each segment.
#
# An IP address consists of 4 numbers, separated from each other with a full stop. But
# your program should just count however many are entered
# Examples of the input you may get are:
#    127.0.0.1
#    .192.168.0.1
#    10.0.123456.255
#    172.16
#    255
#
# So your program should work even with invalid IP Addresses. We're just interested in the
# number of segments and how long each one is.
#
# Once you have a working program, here are some more suggestions for invalid input to test:
#    .123.45.678.91
#    123.4567.8.9.
#    123.156.289.10123456
#    10.10t.10.10
#    12.9.34.6.12.90
#    '' - that is, press enter without typing anything
#
# This challenge is intended to practise for loops and if/else statements, so although
# you could use other techniques (such as splitting the string up), that's not the
# approach we're looking for here.

ipAddress = input("Please input an IP address: ")
segmentSize = 0
segmentNumber = 0
segment = []
for char in ipAddress:
    if char != ".":
        segmentSize += 1
    elif char == ".":
        segmentNumber += 1
        print(f"Segment Number: {segmentNumber}; Segment Size: {segmentSize}")
        # segment.append(segmentSize)
        segmentSize = 0
if ipAddress[-1] != ".":
    # segment.append(segmentSize)
    print(f"Segment Number: {segmentNumber}; Segment Size: {segmentSize}")
for index in range(0, len(segment)):
    print(f"Segment Number: {index+1}; Segment Size: {segment[index]}")

