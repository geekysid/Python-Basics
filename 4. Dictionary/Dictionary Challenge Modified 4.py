# Once that is working, update vocabulary dictionary that also contains number of location that players may use.
# These number will be the keys, and their values will be a single letter that the program can use to determine which
# way to go.

locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

# Here we simply converted list to dictionary by using index of list as the key of the map. This makes our code work
# without any change
exits = {0: {"Q": 0},
         1: {"W": 2, "2": 2, "E": 3, "3": 3, "N": 5, "5": 5, "S": 4, "4": 4, "Q": 0},
         2: {"N": 5, "5": 5, "Q": 0},
         3: {"W": 1, "1": 1, "Q": 0},
         4: {"N": 1, "1": 1, "W": 2, "2": 2, "Q": 0},
         5: {"S": 1, "1": 1, "W": 2,"2": 2,  "Q": 0}}

# Creating new dictionary to map keys of exits[] dictionary with the word enter by user
vocabulary = {"NORTH": "N",
              "EAST": "E",
              "WEST": "W",
              "SOUTH": "S",
              "QUIT": "Q",
              "1": 1,
              "2": 2,
              "3": 3,
              "4": 4,
              "5": 5
              }

loc = 1

while True:
    print()
    # Using join() to fetch and converts all the keys of the exits[loc] dictionary
    availableMovements = ", ".join(exits[loc].keys())
    print(f"{locations[loc]}")
    userInput = input("Available Movements Are: {}\nPlease enter where you wnt to move: ".format(availableMovements)).upper()

    # Checking if user has input a character or a word. If inout is a  word then it will search for it in 'vocabulary'
    # dictionary key and mapping key's value to the user input
    if len(userInput) > 1 and userInput.upper() in vocabulary:
        userInput = vocabulary[userInput]

    # checking if the direction entered by user or not
    if userInput in exits[loc].keys():
        loc = exits[loc][userInput]
        # if user press 'Q' and want to exit
        if loc == 0:
            print("You have successfully exited game.")
            break
    else:   # if user enters invalid direction
        print("That is not a valid movements. Please try again.")
        continue
