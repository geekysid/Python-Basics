print("SET OPERATIONS")

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {2, 4, 6, 8, 10}
setC = {"2", "4", "6", "8"}

print(f"SetA : {setA}")
print(f"SetB : {setB}")
print(f"SetC : {setC}")

print()

print("==UNION (|)==")  # returns every elements in two sets
print(f"setA.union(setB): {setA.union(setB)}")
print(f"setA | setB: {setA | setB}")
print(f"setB | setA: {setB | setA}")
print()
print("==INTERSECTION (&)==")  # returns only common elements in two sets
print(f"setA.intersection(setB): {setA.union(setB)}")
print(f"setA & setB: {setA & setB}")
print(f"setB & setA: {setB & setA}")
print()
print("==DIFFERENCE (-)==")  # returns elements of one set which are not in 2nd sets
print(f"setA.difference(setB): {setA.difference(setB)}")
print(f"setA - setB: {setA - setB}")
print(f"setB - setA: {setB - setA}")
print()
print("==SYMMETRIC_DIFFERENCE (^)==")  # returns set of elements in in 2 sets except those that are common in both.
print(f"setA.symmetric_difference(setB): {setA.symmetric_difference(setB)}")
print(f"setA ^ setB: {setA ^ setB}")
print(f"setB ^ setA: {setB ^ setA}")
print()
print("==ISSUBSET==")   # returns True if every element of 1st set is also available in set 2 else returns False
print(f"setA.issubset(setB): {setA.issubset(setB)}")
print(f"setB.issubset(setA): {setB.issubset(setA)}")
print()
print("==ISDISJOINT==")     # returns True if no element of in 2 sets are common else returns False
print(f"setA.isdisjoint(setB): {setA.isdisjoint(setB)}")
print(f"setB.isdisjoint(setA): {setB.isdisjoint(setA)}")
print(f"setC.isdisjoint(setA): {setC.isdisjoint(setA)}")
print(f"setC.isdisjoint(setB): {setC.isdisjoint(setB)}")
print()
print("==DIFFERENCE_UPDATE==")  # this functions acts similar to difference() but instead of returning a value,
                                # its updates the set to the value
setA.difference_update(setB)
print(f"setA.difference_update(setB): {setA}")
print()
