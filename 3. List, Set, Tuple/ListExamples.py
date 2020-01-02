print("LIST EXAMPLES")

# Example 1: Convert Float to digit list
print("EXAMPLE 1: Convert Float to digit list")
floatNumber = input("Please enter a Decimal Number: ")
digitList = []
for char in str(floatNumber):
    if char.isdigit():
        digitList.append(char)
print(f"digitList: {digitList}")

print()

# Example 2: Convert string List to Nested Character List
print("EXAMPLE 2: Convert string List to Nested Character List")
inputString = input("Please enter a string: ")
dummyList = []
nestedList = []
for char in inputString:
    if char.isalpha():
        dummyList.append(char)
    elif char.isnumeric():
        dummyList.append(char)
    else:
        nestedList.append(dummyList)
        dummyList = []
        continue

if inputString[-1] != " ":
    nestedList.append(dummyList)
print(nestedList)

print()

# Example 2B
test_list = ["a, b, c", "gfg, is, best", "1, 2, 3"]
# we need this output [[‘a’, ‘b’, ‘c’], [‘gfg’, ‘is’, ‘best’], [‘1’, ‘2’, ‘3’]]
finalList = []
dummyList = []
dummyStr = ""
for text in test_list:
    text += ","
    for char in text:
        if char != "," and char != " ":
            dummyStr += char
        elif char == ",":
            dummyList.append(dummyStr)
            dummyStr = ""
    finalList.append(dummyList)
    dummyList = []
print(finalList)

print()
print("Above problem in 2 steps")
for char in test_list:
    dummyList.append(char.split(", "))
print(dummyList)

print()

# Example 3 : Subtracting 2 list
# The original list 1 : ['gfg', 'is', 'best', 'for', 'CS']
# The original list 2 : ['preferred', 'is', 'gfg']
# The Subtracted list is : ['best', 'for', 'CS']
list1 = ['gfg', 'is', 'best', 'for', 'CS']
list2 = ['preferred', 'is', 'gfg']
subtractedList = ['best', 'for', 'CS']

print(f"EXAMPLE 3: Subtract list 1 from list2 and print the result")
print(f"list1: {list1}")
print(f"list2: {list2}")
for char in list2:
    if list1.count(char) > 0:
        list1.remove(char)
print(f"Subtracted List : {subtractedList}")

print()

# Example 4: Swap every consecutive character in a string
print("Example 4: swap every consecutive character in a string")
originalString = "abcdefghij"
swappedString = ""
swappedList = list(originalString)
if len(originalString) % 2 == 0:
    for index in range(0, len(originalString)):
        if index % 2 == 0:
            swappedList[index + 1] = originalString[index]
        else:
            swappedList[index - 1] = originalString[index]
for char in swappedList:
    swappedString += char
print(swappedList)
print(swappedString)

print()

# Example 5: add to the program below so that if it finds meal without a 'spam', it prints iut each of the
# ingredients of the meal.

menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "egg"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["egg", "sausage", ])
menuNumber = 0
print("Example 5: Ingredients in mean without 'spam'")
for meal in menu:
    menuNumber += 1
    if "spam" not in meal:
        print(f"Menu Number: {menuNumber}")
        for ingredients in meal:
            print(ingredients)

print()

# Example 6: Create a list of items (you may use either strings or numbers in the list), then create an iterator
# using the iter() function.
#
# Use a for loop to loop "n" times, where n is the number of items in your list. Each time
# round the loop, use next() on your list to print the next item.
print("Example 6: understanding iter() function")
studentList = ["Siddhant", "Manish", "Kanai", "Shilpa", "Ram", "Mukesh", "Vikash", "Pushpendra"]
student = iter(studentList)
print(f"Location of student: {student}")
print("Printing using iter()")
for i in range(0, len(studentList)):
    print(next(student))
print("Printing using for loop directly")
for item in studentList:
    print(item)
