# functions are defined by the keyword 'def' followed by function name and its parameters it accepts in brackets
print("FUNCTION DEFINITION")
print("functions are defined by the keyword 'def' followed by function name and its parameters it accepts in brackets")


def first_program():
    print("My 1st function")


first_program()  # calling function

print()

print("Every function in Python returns something. If no return statement is present in function,"
      "then by default it returns None")


def return_function():
    return "this functions returns string"


print(first_program())  # this will print as the functions dose'nt return anything.
print(return_function())  # this function will print "this functions returns string" returned from the function called

print()

print("Function that does something")


# A method can hold and execute any set of codes.
def addition():
    num1 = input("Enter 1st number: ")  # inputting data from user inside a function
    num2 = input("Enter 2nd number: ")
    return int(num1) + int(num2)


print("Calling addition() function:")
print(f"Output of addition() is : {addition()}")

print()
print("=+" * 30)
print()


# FUNCTION PARAMETERS
# We can pass one or more value(s) to a function which function can process and use in code. We do this by
# passing an argument to the function while calling it. We can only pass arguments to function which has
# parameters defined inside brackets during defining an function.

# Example of function definition with parameters

def func_with_para(text):
    print(f'Value passed= {text}')


func_with_para('Siddhant')

print()


# Similarly we can have function with n number of parameters each separated by comma. A function call must have
# exactly same number of argument as in function definition else we get an error

def func_with_para(text1, text2, text3, text4):  # funtion that takes 4 parameters
    print(f'This function accepts 4 arguments and the valued passed to function during function call are = '
          f'{text1}, {text2}, {text3} and {text4}')


func_with_para('Argument 1', 'Argument 2', 'Argument 3', 'Argument 4')  # calling function with 4 parameters

print()


# Example 1 : Printing a triangle of * using a function call and for loop
def center_text(num_of_lines, text):
    position = (num_of_lines - len(text)) // 2
    print(" " * position, text)


height_triangle = int(input("Enter height of the triangle: "))
for i in range(1, height_triangle * 2, 2):
    center_text(height_triangle * 2, ("*" * i))

print()
print("=+" * 30)
print()


# *ARGS
# In Python, we have an option of passing any number of arguments to a function call provided function definition
# has *args as a parameter. Here, whatever number of arguments we pass during function call is stored in 'args' in
# the form of tuple

def sum_of_number(*number):
    print(f"args Tuple has: {number}")
    total = 0
    for num in number:
        total += int(num)
    return str(total)


print(f"Sum: {sum_of_number(1, 2, 3, 4, 5, 6)}")

print()
print("=+" * 30)
print()

# NAMED PARAMETERS
# Python provides an option called name parameters. This allows us to pass argument using this name. This
# parameters are mainly used when a function already have *args parameter. We need to provide default value
# to the named value when they are defined in function definition. he named parameters are optional and if
# they are passed in function call then name parameter takes default value.

# we are changing our above sum_of_number function to arithmetic function, where it accepts n number of number
# and an operator
def arithmetic(*number, operator='+'):  # function that take *arg and and an named parameter, operator.
    # This named operator is optional and will take default value of + if it is not passed in function call.
    output = number[0]
    if operator == '+':
        for num in number[1:]:
            output += num
    elif operator == '-':
        for num in number[1:]:
            output -= num
    elif operator == '*':
        for num in number[1:]:
            output = output * num
    elif operator == '/':
        for num in number[1:]:
            output = output / num
    return output

print(f"Add 10, 5 and 2: {arithmetic(10, 5, 2)}")   # calling function without passind value to named parameter, operator. Default valeu of '+' is set to the naned parameter
print(f"Subtract 10, 5 and 2: {arithmetic(10, 5, 2, operator='-')}")    # named parameter value set to '-'
print(f"Multiple 10, 5 and 2: {arithmetic(10, 5, 2, operator='*')}")    # named parameter value set to '*'
print(f"Divide 10, 5 and 2: {arithmetic(10, 5, 2, operator='/')}")    # named parameter value set to '/'

print()
print("=+" * 30)
print()

