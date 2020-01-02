# LIST
print("LIST\n")

# List in Python is similar to other languages. It is same as array. It is group of elements binned together and and
# can be accessed by their index. These element can be of similar data types of different data types. A list can have
# another list inside it, such list are called multilevel lists.

# List with String elements
shoppingList = ["Milk", "Bread", "Butter", "Oil"]
print(f"List with String elements:\n{shoppingList}\n")

# List with Integers elements
numberList = [101, 202, 303, 404, 505, 606, 707]
print(f"List with Integer elements:\n{numberList}\n")

# List with Float elements
floatList = [1.01, 20.2, .303, 404., 5.05]
print(f"List with Float elements:\n{floatList}\n")

# List with Mixed elements
mixedList = ["Milk", 202, .303]
print(f"List with Mixed elements:\n{mixedList}\n")

# Fetching elements of list using index
print("Fetching elements of list using index")
for index in range(0, len(shoppingList)):
    print(shoppingList[index])

print()

# List Slicing
print("LIST SLICING")
# We can slice list in the same way we slice strings. We use [startIndex:endIndex:step] to slice a list.
# In below example we will create a new list by slicing the list created above from index 1 to index 3
slicedList = shoppingList[1:3]
print(f"Sliced List: {slicedList}")

print()

# Reversing List
print("RESERVING LIST")
print(f"Reversing numberList list using [::-1]:\n{numberList[::-1]}")

print()

# Mutable List
print("LIST ARE MUTABLE")
# Unlike strings, list are mutable abd there elements can be changed using indices.
studentList = ["Siddhant", "Manish", "Kanai", "Shilpa", "Ram"]
print(f"Original List:\n{studentList}")
studentList[3] = "Abhishek"
print(f"List after changing 3rd element:\n{studentList}")

print()

# Adding element to list
print("ADDING ELEMENT TO LIST")
print("\tappend()")
print(f"Original List: \n{studentList}")
# We can add elements to a list in 3 ways
# Append() - This method basically add element(exactly one) to the end of the list
studentList.append("Prem")
print(f"\tList after appending(append()) an element at the end of list:\n\t{studentList}")

print()

# We can also use method insert() to add new element at a given indices in list
print("\tinsert()")
studentList.insert(0, "Vikash")
print(f"\tList after inserting (insert()) an element at a given index (0 in our case) of list:\n\t{studentList}")

print()

# We also have a method called extend(). This method can add another list to current list at the end
print("\textend()")
newAddition = ["Mukesh", "Pushpendra", "Rohit"]
studentList.extend(newAddition)
print(f"\tList after extending (extend()) list by another list of 3 elements:\n\t{studentList}")

print()

# Removing element from list
print("REMOVING ELEMENT FROM LIST")
numberList = [1, 2, 3, 4, 2, 5, 6, 3, 4, 9]
print(f"Original List: \n{numberList}")

# We use method remove() to remove the 1st occurrence of item passed as an argument to this method
print("\tremove()")
numberList.remove(2)
print(f"\tList after using remove() to remove 2 from list:\n\t{numberList}")

# to delete element at a particular indices in the list we can use the keyword del
print()
print("\tdel keyword")
del numberList[4]
print(f"\tWe can delete element @ 4th index of the list using 'del numberList[4]:\n\t{numberList}")
# with del keyword we can delete multiple elements by proving starting index and end index. It is important to note
# that element end index will not be deleted. Deletion will continue up to (end index - 1)
del numberList[1:5]
print(f"\tWe can delete element from 1st index to 5th index of the list using 'del numberList[1:5]' :\n\t{numberList}"
      f"\n\tIt is important to note that element @ 5th index will not be deleted. Deletion will continue up to 4th "
      f"index")
# we can also delete the entire list using keyword del
del numberList
print(f"\tWe have deleted entire list by using 'del numberList'. We will get an error if we try to access 'numberList'")

print()
print("\tpop()")
# we use this method to remove last element from a given index (passed in argument of menthod or at the end of list
# if no argument is passed in the method.
print(f"\tStudentList: {studentList}")
studentList.pop()
print(f"\tStudent list by using pop():\n\t{studentList}")
studentList.pop(0)
print(f"\tStudent list by using pop(0):\n\t{studentList}")

print()
print("\tRemoving element by Slicing of List")
studentList[2:4] = []
print(f"\tList after slicing element @ 2nd, 3rd and 4th index of the list:\n\t{studentList}")

print()
print("\tclear()")
# This method is used to empty the string but the list is not delete and exist as an empty list unlike del keyword.
studentList.clear()
print(f"\tStudent list by using clear():\n\t{studentList}")

# SORTING OF LIST
print("SORTING OF LIST")
# We can use sort function to sort the list
numberList = [1, 2, 3, 4, 2, 5, 6, 3, 4, 9]
print(f"Before Sorting: {numberList}")
numberList.sort()
print(f"After Sorting: {numberList}")

# to reverse the order of sorting
numberList = [1, 2, 3, 4, 2, 5, 6, 3, 4, 9]
print(f"Before Sorting in reverse: {numberList}")
numberList.sort(reverse=True)
print(f"After Sorting in reverse order: {numberList}")

# REVERSING OF LIST
print("\nSORTING OF LIST")
# We can use reverse function to reverse the list
numberList = [1, 2, 3, 4, 2, 5, 6, 3, 4, 9]
print(f"List  Before Reverse: {numberList}")
numberList.reverse()
print(f"List After Reverse: {numberList}")

print()

# MAX(), MIN() SUM()
# We can use max() and sum() function only on list with int or decimal elements
print(f"using max(numberList) we get: {max(numberList)}")
print(f"using min(numberList) we get: {min(numberList)}")
print(f"using sum(numberList) we get: {sum(numberList)}")
