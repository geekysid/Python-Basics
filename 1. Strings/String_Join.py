myList = ["a", "b", "c", "d", "e"]
myStringUsingLoop = ""

for item in myList:
    myStringUsingLoop += (item + ", ")

print(f"String : {myStringUsingLoop}")

print()

myStringUsingJoin = ""
myStringUsingJoin += ", ".join(myList)
print(f"concatenation using join(): {myStringUsingJoin}")

print()

name = "Siddhant"
myStringUsingJoin = ""
myStringUsingJoin += ", ".join(name)
print(f"concatenation using join() on string: {myStringUsingJoin}")

print()

name = "Siddhant is a python developer"
myStringUsingJoin = ""
myStringUsingJoin += ", ".join(name)
print(f"concatenation using join() on string: {myStringUsingJoin}")

