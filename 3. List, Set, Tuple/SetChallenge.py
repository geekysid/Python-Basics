# Create a program that takes some text and returns a list of all the characters in the text that are not vowels,
# sorted in alphabetical order.
#
# You can either enter the text from the keyboard or initialise a string variable with the string.

# Method 1
userInput = input("Please enter a string of text: ")
vowels = {"a", "e", "i", "o", "u"}
inputSet = set()

if len(userInput) > 1:
    inputList = userInput.split()
    for word in inputList:
        for char in word:
            if char not in vowels:
                inputSet.add(char)
    print(sorted(inputSet))

# Method 2
userInput = input("Please enter a string of text: ")
vowels = {"a", "e", "i", "o", "u"}
inputSet = sorted(set(userInput).difference(vowels))
print(inputSet)
