locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"S": 1, "W": 2, "Q": 0}]

loc = 1
while True:
    availableMovements = ", ".join(exits[loc])
    print()
    print(locations[loc])
    print("You can move in following directions: {}".format(availableMovements))
    userMovement = input("In which direction would you like to move? ").upper()

    if userMovement in availableMovements:
        if userMovement == "Q":
            print("Thanks for being part of this game.")
            break
        else:
            loc = exits[loc].get(userMovement)
            continue
    else:
        input("This is not a valid movement. Please press enter key to try again.")
        continue
