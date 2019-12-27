# Author: Siddhant Shah
# Descp: Understanding and working with strings


# In Python we can use strings as below
myName = "Siddhant"
print(myName)

# We can place string literals in between single quotes (') or in between double quotes (").
# If we start a string using single quote then it must end with single quote only and if we
# start a quote with double quotes then it must end with double quotes only as shown below.
print("Stepping into world of Python with Double Quotes")
print('Stepping into world of Python with Single Quotes')

# Escape Characters in Strings
print('\nESCAPE CHARACTERS IN STRINGS')
# Like other languages, python also provides escape characters to add some type of formatting to the string
print('This \nString \nUses \nNew Line \nEscape \nCharacter')   # This string uses an special escape character (\n) to
                                                                # add a new line
print('This \tString \tUses \tTab \tEscape \tCharacter')    # This string uses an special escape character (\t) to add
                                                            # tab between characters.
print('This \\String \\Uses \\BackLash \\Escape \\Character')   # This string uses an special escape character (\\) to
                                                                # add backlash between characters
print('This \'String \'Uses \'SingleQuote \'Escape \'Character')    # This string uses an special escape character (\')
                                                                    # to add single quotes between characters
print('This \"String \"Uses \"DoubleQuote \"Escape \"Character')    # This string uses an special escape character (\")
                                                                    # to add double quotes between characters

# If we want to print single quotes in string then instead of using escape characters, we can simply
# define the string using double quotes and vice vera
print("This 'String 'Displays 'SingleQuote 'Without 'Any 'Escape 'Character")
print('"This "String "Displays "DoubleQuote "Without "Any "Escape "Character')

# STRING with INDEX
print('\nSTRINGS WITH INDEX')
# In Python we can fetch different parts of strings using the index. For this we need to assign a variable to the
# string and then access different characters of strigs using index of that character (variableName[idexOfCharacter])
completeString = 'Python is a really useful coding language'
print(completeString)
partOfString = completeString[0]    # fetching the 3rd character from sting stored in 'completeString' variable.
                                    # It is important to note that indices for a string starts from 0 (left to right),
                                    # i.e. index for the 1st character of the string is always 0, 2nd character is 1
                                    # and so on
print(partOfString)
partOfString = completeString[1]
print(partOfString)
partOfString = completeString[2]
print(partOfString)

# Negative indices in String
print('\nNEGATIVE INDEXES IN STRINGS')
# We can even use negative numbers as indices to fetch part of string. In this case the last character of the
# string is represented as -1, second last character is -2 and so on
completeString = 'Python is a really useful coding language'
print(completeString)
partOfString = completeString[-1]    #fetching the last character from sting stored in 'completeString' variable.
                                    # It is important to note that negative indices for a string starts from -1
                                    # (right to left), i.e. index for the last character of the string is always
                                    # -1, 2nd last character is -2 and so on
print(partOfString)
partOfString = completeString[-2]
print(partOfString)
partOfString = completeString[-3]
print(partOfString)
partOfString = completeString[-4]
print(partOfString)


# Slicing of String
print('\nSLICING OF STRINGS')
# So far we have seen how to access each characters of strings. In python we can even access part of strings instead
# of a single character. We do it by what we call SLICING OF A STRING. [start:stop:step]. Using this we can access any
# part of string that we need.
completeString = 'Lets slice this string'
print(completeString)
print(completeString[1:4])      # slicing string form character with index 1 upto character with index 4. (Character
                                # with index 4 is not included)
print(completeString[5:])       # slicing string form character with index 5 upto end
print(completeString[:6])       # slicing string form start of string upto character with index 6. (Character with
                                # index 6 is not included)
print(completeString[2:15:3])   # slicing string form character with index 2 upto character with index 15. Here only
                                # the 3rd charcter will be part of sliced string and all other characers will be
                                # skipped. So here we will have characters with indices 2,5,8,11 and 14
print(completeString[2:15:2])   # slicing string form character with index 2 upto character with index 15. Here only
                                # the 2nd charcter will be part of sliced string and all other characers will be
                                # skipped. So here we will have characters with indices 2, 4, 6, 8, 10, 12 and 14
print(completeString[::-1])
print(completeString[-10:-1])

# Immutable String
print('\nSTRINGS are IMMUTABLES')
# Even though we can  access different part/characters of strings using indexes and slicing, we cant change string.
# This makes strings Immutables.
string1 = "This is String 1"
string2 = string1[:-1] + "2"    # here we slice the string and used concatenation to change the string.
print(string2)

days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print('Mon' in days)

# Exercise: String = "abcdefghijklmnopqrstuvwxyz"
# Create a slice that produce characters qpo
# Create a slice that produce characters edcba
# Create a slice that produce last 8 characters in reverse order
print("Exercise")
alphabets = "abcdefghijklmnopqrstuvwxyz"
print(alphabets[-12:-9][::-1])
string2 = alphabets[:5]
print(string2[::-1])
print(alphabets[26:17:-1])

# STRING REPLACEMENT
# In python every datatype can be converter into String.  we can use function str() to convert anything into string.
print('STRING REPLACEMENT')
num1 = 12
num2 = 13
print(num1 + num2)      # Hete '+' performs the task of simple addition
print(str(num1) + str(num2))    # after converting num1 and num2 to string we can see that the two string just
                                # concatenates instead of adding together as in previous command

# STRING REPLACEMENT
# Python provides a function 'format()' which we can use with string to provide value to a placeholder'{}' dynamically.
print('STRING REPLACEMENT')
name = "Sid"
age = 22
print('your name is {} and your age is {}'.format(name, age))   # Here we have two place holder '{}' and we have provided
                                                                # value to the two place holders by passing an arguments
                                                                # to the format function. It is important to note that
                                                                # the placeholders takes arguments in sequential way if
                                                                # not mentioned oher way. In next command we will provide
                                                                # indexes in placeholders. These indices willindicate the
                                                                # which argument will be placed in place holder

print('Your name is {0} and your age is {1}'.format(name, age)) # Here we can see that we have provided indices to
                                                                # placeholders to indicate which arguments passed in
                                                                # format function will be placed in which place holder

print('Your name is {1} and your age is {0}'.format(age, name)) # Here we can see that even though arguments in format
                                                                # funtion is not in proper sequesnce, the indices used in
                                                                # placeholders make sure that we get the proper value in
                                                                # each placeholder

print('Your name is {n} and your age is {a}'.format(a=age, n=name)) # Here we have given a proper name to to each argument
                                                                    # in format function and used those names as indices in
                                                                    # placeholders. This is really an easy way to make sure
                                                                    # we have placed correct value in each placeholder

# Examples
print('We can {r} {r} {r} any that can be {fun}'.format(r='repeat', fun='fun', h='hahaha'))
print("Jan: {2} Days, Feb: {0} Days, Mar: {2} Days, Apr: {1} Days, May: {2} Days, Jun: {1} Days, Jul: {2} Days".format(28,30,31))
print("""Jan: {2} Days
        Feb: {0} Days
        Mar: {2} Days
        Apr: {1} Days
        May: {2} Days
        Jun: {1} Days
        Jul: {2} Days""".format(28,30,31))

# STRING FORMATTING We can use string formatting in order for proper alignment or decimal places or white spaces before
# or after any digit. We cn achieve this by using {index:width.FloatingNumber}. Index is the positing of arguments
# passed in format function, width is the the total place that the value will take (if width provided is more then the
# characters of value then we'll have white space (and if width is less then total characters in value then also we will
# have all characters displayed) and last but not the least, Floating Number is the total number of characters that
# will be displayed after decimal. It is important to note that floating number can oly be associated with  integer or
# decimal. We get an error if floating number is provided for string. If decimal numbers are less then number of
# floating number then for ever extra number we will have 0 place at the end. If floating number is less then the
# digits after decimal then digits will be rounded off according to floating number.

# We can even specify left, right or center alignment of the value using '<', '>', or '^' respectively after colon(:)
# and before width. We will see example of all these below.
print('\nSTRING FORMATTING')

print("We are simply using for loop (will study about it later) to print number and its square and cube value.")
for i in range (2, 6):
    print('No. {0} has square value of {1} and cube value of {2}'.format(i, i**2, i**3))

print()
print("Now we are providing width for every value. the 1st placeholder will have width of 1 digit, 2nd will have\n"
      "width of 2 digits and 3rd will have width of 3 digits. Notice that output will be right aligned by default\n "
      "even though we have not provided any '>' operator.")
for i in range(2,6):
    print('No. {0:1} has square value of {1:2} and cube value of {2:3}'.format(i, i**2, i**3))

print()
print("""Here we, along with providing width of to the placeholder, we have also provided alignment operators.
The 1st placeholder has ^ operator which signifies center alignment, 2nd placeholder has < that signifies
left alignment and 3rd placeholder have > which signifies right alignment""")
for i in range(2,6):
    print('No. {0:1} has square value of {1:<2} and cube value of {2:>3}'.format(i, i**2, i**3))

print()
print("""In this section we have increased the width of each place holder to 5 digits and used same alingmnet
operators as in last section to see the difference""")
for i in range(2,6):
    print('No. {0:^5} has square value of {1:<5} and cube value of {2:>5}'.format(i, i**2, i**3))

print()
print("""In this section we will test the floating numbers along with width. We have given 2 floating number to 1st
placeholder, 3 floating number to 2nd place holder and 4 to 3rd place holder. As any of our value have no 
decimal points, so each value is followed by n number of 0 after decimal point where n is value of floating number.""")
for i in range(2,6):
    print('No. {0:1.2f} has square value of {1:<8.3F} and cube value of {2:>9.4f}'.format(i, i**2, i**3))

print()
print("""Here we will see another example of floating number.""")
print("""Value of PI: {0:5}
Value of PI: {0:5.3f}
Value of PI: {0:5.2f}
Value of PI: {0:5.0f}
Value of PI: {0:5.60f}""".format(22/7))

# f STRINGS
# f String, also known as Formatted Strings is another way or rather a faster and easier way to format string. Here
# instead of using format function we simply pass the value along with width and floating expression directly into
# placeholder. We do this by placing 'f' before the starting of string (before quote) as shown below. Also the
# formatting of the string is exactly same as before. Lets dive into examples....
print("\nf STRINGS")
for i in range(2,6):
    print(f"No. {i} has square value of {i**2} and cube value of {i**3}")
print()
for i in range(2,6):
    print(f"No. {i:2} has square value of {(i**2):3} and cube value of {i**3:4}")
print()
for i in range(2,6):
    print(f"No. {i:^3} has square value of {(i**2):<3} and cube value of {i**3:>4}")
print()
for i in range(2,6):
    print(f"No. {i:^5.2f} has square value of {(i**2):<6.3f} and cube value of {i**3:>8.4f}")
print()
pi=22/7
print(f"""Value of PI: {pi}
Value of PI: {pi:6}
Value of PI: {pi:6.0f}
Value of PI: {pi:6.2f}
Value of PI: {pi:6.60f}
""")

# STRING FUNCTIONS
print("STRING FUNCTIONS")
string1 = "This is a string"
print("Our string is " + string1 + "\n")
print("Using function upper() to convert string to upper case\nstring1.upper(): " + string1.upper())
print("\nUsing function lower() to convert string to lower case\nstring1.lower(): " + string1.lower())
print(f"\nUsing function isupper() returns true if string has only upper case letter\nstring1.isupper(): "
        f"{string1.isupper()}")
print(f"\nUsing function capitalize() returns string with 1st character as capital\nstring1.capitalize(): "
        f"{string1.capitalize()}")
print(f"\nUsing function count() returns number of times string literal passed as an argument appear in "
        f"string\nstring1.count('s'): {string1.count('s')}")
print(f"\nUsing function endswith() returns true if string ends with string literal passed as an argument "
        f"\nstring1.endswith('ng'): {string1.endswith('g')}")
print(f"\nUsing function isnumeric() returns true if string is numeric else returns false\nstring1.isnumeric(): "
        f"{string1.isnumeric()}")
print(f"\nUsing function isalpha() returns true if string is numeric else returns false\nstring1.isalpha(): "
        f"{string1.isalpha()}")
print(f"\nUsing replace() function, we can replace characters in given literal\nstring1.replace('string', 'literals'): "
      f"{string1.replace('string', 'literals')}")
print(f"\nUsing split() function, we can split the string whenever a literal passed in the argument appears in \n"
      f"the string. 2nd argument is optional and signifies number of times the string will be splitted.\nstring1.split("
      f"'s'): {string1.split('s')}")
print(f"\nUsing strip() function, we can remove the string literals passed in the argument of the function. It is "
      f"\nimportant to note that the literals passed as arguments must be the starting literals of the string else it "
      f"\nwont work. if no argument is passed then the space is removed if it is at the beginning of the "
      f"string.\nstring1.strip('This'): {string1.strip('This')}")
print(f"\nUsing index() function, we get index of1st occurence of the literal passed in the argument of the function. "
        f"Itis important to note that the 2nd and 3rd arguments are option and signifies starting and ending point from"
        f"\nwhere the search will start and end.\nstring1.index('s',2,10): {string1.index('s',2,10)}")
