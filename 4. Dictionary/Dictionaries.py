# Dictionaries is unordered sequence of key-value pair with unique key set. Keys can be of different data types and
# so can be values. Here is an example of dictionary
myDict = {1: "One",
          2: "Two",
          3: "Three",
          4: "Four",
          5: "Five",
          }
myDict2 = {"a": "Apple",
           "b": "Boy",
           "c": "Cat",
           "d": "Doctor",
           }

print("SIMPLY PRINTING DICTIONARY")
# Printing the entire dictionary
print("myDict = {}".format(myDict))
print("myDict2y = {}".format(myDict2))
print("using for loop using keys")
for x in myDict:
    print(myDict[x], end=" ")
print()
print("using for loop using values")
for x in myDict.values():
    print(x, end=" ")
print()

print()

print("LOOPING THROUGH DICTIONARY")
# Looping through dictionary
for key in myDict:
    print(f"{key:>2} = {myDict[key]:<7}")
print("=" * 20)
for key in myDict2:
    print(f"{key:>2} = {myDict2[key]:<7}")

print()
print("ACCESSING VALUE FROM A DICTIONARY")
# In above example, 1,2,3,4,5 are keys and "One", "Two", "Three", "Four" and "Five" are their respective values.
# We can fetch the value in dictionary by using its keys as below
print("===get()===")
print(f"myDict[2]: {myDict[2]}")    # Here 2 is the key and not the index.
print(f"myDict2['a']: {myDict2['a']}")
print("Using get() to fetch value form index. Even if we pass an invalid index as argument in get() , we get 'None' as "
      "output")
print(f"myDict2get('a'): {myDict2.get('a')}")
print(f"myDict2get('z'): {myDict2.get('z')}")
print(f"myDict2get('z'): {myDict2.get('z', 'We dont have a element in dictionary with key z')}")
print()
print("CHANGING VALUE IN A DICTIONARY")
# We can change the value associated to any key as below
myDict[2] = "This is updated values"
print(f"myDict[2] = {myDict[2]}")
print(f"myDict2['c'] = {myDict2['c']}")

print()

print("FETCHING ALL KEYS & VALUES IN A DICTIONARY SEPARATELY")
print("=" * 3 + "Keys" + "=" * 3)
print(myDict.keys())
keyList = myDict.keys()
# print(keyList[0])
print("=" * 3 + "Values" + "=" * 3)
print(myDict.values())
valuesList = myDict.values()
# print(valuesList)

print()

print("DICTIONARY WITH LIST")
myDict3 = {"a": "Hello",
           "b": "how",
           "c": "are",
           "d": "you",
           "e": ["baby", "honey", "friend"]
           }
print(myDict3)
print(f"myDict3['e'][0]: {myDict3['e'][0]}")

print()

print("REMOVING ELEMENTS FROM DICTIONARY")

originalDict = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}
print("originalDict: {}".format(originalDict))
print("**pop()** function removes the key value pair from the dictionary and returns the value of the key passed in "
      "the function")
popValue = originalDict.pop(5)
print("Dictionary after pop(5) = {}".format(originalDict))
print("popValue = originalDict.pop(5) gives {}".format(popValue))

print("**popitem()** function removes an arbitrary key value pair from the dictionary and returns the element as "
      "tuples")
popItemValue = originalDict.popitem()
print("Dictionary after popitem() = {}".format(originalDict))
print("popValue = originalDict.popitem() gives {}".format(popItemValue))

print("**del** keyword the element from the dictionary whose key is provided in the []")
del originalDict[3]
print("Dictionary after 'del originalDict[3]' = {}".format(originalDict))
print("We need to be careful when dealing with 'del' keyword as if we forget to add the key to the dictionary then "
      "entire dictionary will be deleted and even variable name will ase to exist")
print("**clear()** function empty the dictionary and deletes all the key-value pair it has")
originalDict.clear()
print("Dictionary after 'originalDict.clear()' = {}".format(originalDict))

print()

print("JOINING  TWO DICTIONARY")
dict1 = {}
dict2 = {}
for x in range(1, 11):
    if x % 2 == 0:
        dict1[x] = x*x
    else:
        dict2[x] = x*x
print("dict1 = {}".format(dict1))
print("dict2 = {}".format(dict2))
dict1.update(dict2)
print("dict1.update(dict2) = {}\nupdate() dose'nt return anything.".format(dict1))

print()

print("SORTING DICTIONARY")
print("**sorted()**")
# dict1.sort()
# print("sorted(dict1) = {}".format(sorted(dict1)))

print()

print("NESTED DICTIONARY")
nestedDict = {"a": "Hello",
              "b": "how",
              "c": "are",
              "d": "you",
              "e": {"a": "baby",
                    "b": "honey",
                    "c": "friend"
                    }
              }
print(nestedDict)
print(f"nestedDict['e']['b']: {nestedDict['e']['b']}")

print()
print("=x=" * 10)
print()
originalDict = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}

print("DICTIONARY FUNCTIONS")
print("dict() - This function converts list into dictionary with index as keys and elements as values")
# originalDict = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}
# myList = ["One", "Two", "Three", "Four", "Five"]
# resultantDict = dict(myList)
# print(f"resultantDictDict = {dict(myList)}")

print()
print("=x=" * 10)
print()

# # Example 1: take user inout between 1-10 and display its square root from dictionary
#
# print("EXAMPLE 1: Take user inout between 1-10 and display its square root from dictionary")
# squareDict = {}
# for x in range(1, 11):
#     squareDict[x] = x*x
# print(f"Original Dict: {squareDict}")
# flag = True
# while flag:
#     userInput = input("Please enter number between 1-10 for its square value: ")
#     if userInput.isnumeric():
#         if int(userInput) == 0:
#             flag = False
#         elif int(userInput) not in squareDict:
#             print("Man '{}' is not between 1-10. Are you our of mind??".format(userInput))
#             continue
#         else:
#             print("Square of {} is {}".format(userInput, squareDict.get(int(userInput))))
#     else:
#         print("Man '{}' is not even a number. Go and learn numbers and alphabets??".format(userInput))
#         continue

print()
print("=x=" * 10)
print()

print("DICTIONARY KEYS AS LIST")
print("Original Dictionary: {}".format(dict1))
keyList = list(dict1.keys())
print("List of Keys in dict1: {}".format(keyList))
print("Sorted Key List: {}".format(sorted(keyList)))

print()

print("DICTIONARY VALUES AS LIST")
print("Original Dictionary: {}".format(dict1))
valueList = list(dict1.values())
print("List of Keys in dict1: {}".format(valueList))
print("Sorted Value List: {}".format(sorted(valueList)))

print()
print("=x=" * 10)
print()

print("dict_key VIEW")
print("Whenever we use keys() or values() functions, we get a dict_key view. These view are just an image of keys or "
      "values depending on function used and if there is any change in dictionary then these views also changes"
      "accordingly")
print("Original Dictionary: {}".format(originalDict))
dictKey = originalDict.keys()
dictValue = originalDict.values()
print("On using originalDict.keys() we get : {}".format(dictKey))
print("On using originalDict.values() we get : {}".format(dictValue))
originalDict[6] = "Six"
print("Now when we ad one more key value pair in dictionary, we can see that dict_views also changes")
print("dict_keys: {}".format(dictKey))
print("dict_values: {}".format(dictValue))

print()
print("=x=" * 10)
print()

print("TUPLE FROM DICTIONARY")
print("==items()==")
print("items() function returns dict_view list of tuple.")
print(f"originalDict: {originalDict}")
dict_2_tuple = tuple(originalDict.items())
print(f"Tuple of this dictionary using items() function as originalDict.item() is as below:\n{dict_2_tuple}")
print(f"In order to convert these dict_view into tuple, we can simply typecast it like tuple(originalDict.items()). "
      f"Output will be as below:\n{dict_2_tuple}")
print("Example")
for item in dict_2_tuple:
    numeric, alpha = item
    print(f"{numeric} is {alpha}")

print("CONVERTING TUPLE BACK TO DICTIONARY")
tuple_2_dict = dict(dict_2_tuple)
print(tuple_2_dict)

print()
