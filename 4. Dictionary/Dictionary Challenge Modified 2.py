# Modify the program so that the exits is a dictionary rather than a list, with the keys being the numbers of the
# locations and the values being dictionaries holding the exits (as they do at present). No change should be needed
# to the actual code.

locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

# Here we simply converted list to dictionary by using index of list as the key of the map. This makes our code work
# without any change
exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"S": 1, "W": 2, "Q": 0}}

loc = 1
while True:
    print()
    # Using join() to fetch and converts all the keys of the exits[loc] dictionary
    availableMovements = ", ".join(exits[loc].keys())
    print(f"{locations[loc]}")
    userInput = input("Available Movements Are: {}\nPlease enter where you wnt to move: ".format(availableMovements))
    if userInput.upper() in exits[loc].keys():  # checking if the direction entered by user or not
        loc = exits[loc][userInput.upper()]
        if loc == 0:    # if user press 'Q' and want to exit
            print("You have successfully exited game.")
            break
    else:   # if user enters invalid direction
        print("That is not a valid movements. Please try again.")
        continue
