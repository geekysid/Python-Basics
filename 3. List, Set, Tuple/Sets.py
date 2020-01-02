print("====")
print("SETS")
print("====\n")
print("# Sets are unordered sequence of unique elements where each element is separated by comma(,) inside curly\n"
      "braces '{}'. If any item is repeated in a set then only one instance of it is considered in set and rest is\n"
      "ignored.")

print()

# Simple Set
print("Simple Set Example")
mySets = {1, "2", 3, "4", 5, "6"}
print(f"Set with mixed elements: {mySets}")

print()

# Set with repeated element
print("Simple Set with repeated Element Example")
mySets = {"1", "2", "3", "4", "5", "6", "6"}
print(f"Set with repeated element: {mySets}")
print("We can see that only one instance of '6' is part of set and all other instances are ignored")

print()
# Sets are MUTABLE
print("Sets are MUTABLE")
print("# Set is MUTABLE but cannot have any other mutable elements like list, dictionary or set inside."
      "But set can have immutable tuple")
immutableSet = {1, "2", 3, "4", 5, ("1", "2", "3")}
print(f"Set with tuple: {immutableSet}")

print()

# Converting List to Set
print("# We can convert list to set by simple type casting provided list has no mutable element like list or dictionary")
myList = ["1", "2", "3", "4", "5", "6", "6"]
list2set = set(myList)
print(f"list: {myList}\nList to Set: {list2set}")
print("We can see that even when list have a duplicate element '6' but only one instance of '6' was part of set and "
      "rest was ignored")

print()

# Empty Sets
print ("Generating empty is a bit tricky as {} creates an empty dictionary. So in order to create am empty set,\n"
       "we use the function set()")
mySets = set()
print(f"'mySets = set()' give: {mySets}")

# Changing value of Set
print('# Changing value of Set')
originalSet = {1, "2", 3, "4", 5, ("1", "2", "3")}
print(f"Original Set: {originalSet}")

print("**add()**")
originalSet.add("6")
print(f"After originalSet.add('6'), set changes to:\n{originalSet}")

print("**remove()**")
originalSet.remove("6")
print(f"After originalSet.remove('6'), set changes to:\n{originalSet}")

print("**update()**")
originalSet.update(['hello', 'how', 'are', 'you'])
print(f"After originalSet.update(['hello', 'how', 'are', 'you']), set changes to:\n{originalSet}")
originalSet.update(('This', 'is'), ('wonderful', 'baby'))
print(f"After originalSet.update(('This', 'is'), ('wonderful', 'baby')), set changes to:\n{originalSet}")
print("We can see here that we can add multiple elements using update() but duplicates are ignored.")
print("It is also important to note that even if we pass list or a tuple as an argument in update method,\n"
      "individual elements of the list or tuple are added to the set and not the entire list or tuple.")

print()

# Removing element from Set
print("# Removing element from Set")

print("**remove()**")
print("This functions removes() removes the element (passed as an argument in function) from the set. If the element\n"
      "is not in set then we get an error")
originalSet.remove('This')
print(f"After originalSet.remove('This'), we get:\n{originalSet}")

print("**discard()**")
print("This functions discard() removes an element (passed as an argument in function) from the set. If the element\n"
      "is not in set then we don't get an error")
originalSet.discard('wonderful')
print(f"After originalSet.discard('wonderful'), we get:\n{originalSet}")
originalSet.discard('This')
print(f"After originalSet.discard('This'), we get:\n{originalSet}")

print("**pop()**")
print("This functions pop() removes and return an arbitrary element from the set")
element = originalSet.pop()
print(f"After originalSet.pop('wonderful'), we get:\n{originalSet}")
originalSet.discard('This')
print(f"After originalSet.discard('This'), we get:\n{originalSet}")

print()

print("# SORTING SET")
print("**sorted()**")
setA = {4, 2, 1, 9, 7, 3, 8, 6, 5}
print(f"Unsorted Set: {setA}")
print(f"set(sorted(setA)): {set(sorted(setA))}")

print()

print("# Iterating through SET")
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
for element in setA:
    print(element, end=" ")
