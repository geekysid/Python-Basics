# Ranges: We have used ranges in for loop before. Ranges are basically an object which holds starting and end value of
# integer.

# Ranges can be used as follow
# Example 1
print("When using range(10)")
myRange = range(10)
print(myRange)
for i in myRange:
    print(i, end=" ")

print()

# Example 2
print("When using range(0, 10)")
myRange = (0, 10)
for i in myRange:
    print(i, end=" ")

print()

# Example 3
print("When using range(0, 10, 2)")
myRange = (0, 10)
for i in myRange:
    print(i, end=" ")

print()

# Example 4
print("When using list(range(0, 10))")
myRange = list(range(0, 10))
print(myRange)

print()

# program 1: Input a number from console and check if its divisible by 7 using range
print("Program 1: Input a number from console and check if its divisible by 7 using range")
numbers = range(7, 100, 7)
inputValue = input("Please enter a positive number less then 100: ")
flag = True
while flag:
    if inputValue.isnumeric() and int(inputValue) < 100 and int(inputValue) < 100:
        flag = False
    else:
        inputValue = input("You have entered invalid input.\nPlease enter a positive number less then 100: ")
if int(inputValue) in numbers:
    print("Input number {} is divisible by 7, {} times".format(inputValue, (numbers.index(int(inputValue))+1)))
else:
    print("Inout number {} is not divisible by 7".format(inputValue))

print()

# SLICING RANGES
print("number : {}".format(list(numbers)))
slicedRange = numbers[:10:3]
print("Sliced range using slicedRange = numbers[:10:3] = \n{}".format(list(slicedRange)))
print(f"Index of 28 in numbers: {numbers.index(28)}")
print(f"Index of 28 in slicedRange: {slicedRange.index(28)}")
print(f"Element @ index 3 in numbers: {numbers[3]}")
print(f"Element @ index 3 in slicedRange: {slicedRange[3]}")

print()

print("range(0, 10, 2) == range(0, 9, 2) will give '{}' as they will have same sets of "
      " element".format(range(0, 10, 2) == range(0, 9, 2)))
print("range(0, 10, 2) = {}".format(list(range(0, 10, 2))))
print("range(0, 9, 2) = {}".format(list(range(0, 9, 2))))
print("range(0, 10, 2) == range(0, 11, 2) will give '{}' as they will have different sets of "
      " element".format(range(0, 10, 2) == range(0, 11, 2)))
print("range(0, 10, 2) = {}".format(list(range(0, 10, 2))))
print("range(0, 11, 2) = {}".format(list(range(0, 11, 2))))

print()

myRange = range(0, 50)
slicedRange = myRange[::5]
print(f"SlicedRange: {slicedRange}")
for i in slicedRange:
    print(i)
print('*'*10)
for i in slicedRange[::-1]:
    print(i)

print()