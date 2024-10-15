# Dictionaries
main_menu = {
    "A": "(A)bout the game.",
    "P": "(P)lay Chicago Explorers!",
    "D": "(D)isplay game stats.",
    "Q": "(Q)uit."
}
# a dictionary that defines the relationships/connections between locations
locations_map = {
    'shedd aquarium': ['field museum', 'mccormick place'],
    'mccormick place': ['shedd aquarium', 'museum of science and industry'],
    'museum of science and industry': ['mccormick place'],
    'uic': ['field museum'],
    'field museum': ['uic', 'shedd aquarium', 'art institute'],
    'art institute': ['millennium park', 'willis tower', 'river walk', 'field museum'],
    'willis tower': ['art institute'],
    'millennium park': ['art institute'],
    'navy pier': ['river walk'],
    'river walk': ['art institute', 'navy pier']
}
# dictionary of inspirations - maps location -> message that should be printed
inspirations = {
    'museum of science and industry': 'Surrounded by the inventions of others, you begin to draft new displays of innovation to inspire others',
    'art institute': 'The sculptures within the Art Institute remind you of the intricate stonework in Chicago, you wonder about how you can incorporate this into your project.',
    'willis tower': 'The towering might of this iconic skyscraper has given you new ideas on how to create a new, soaring masterpiece to add to the Chicago skyline.'
}

# String variables that contain output text you print at various points (so you don't have to guess)
welcome_msg = '--- WELCOME TO CHICAGO EXPLORERS ---\n'
about_msg = 'ABOUT THE GAME:\nYou and your party have been asked to come up with Chicago\'s next great landmark!\nTo begin your creative journey, you have all decided to visit the city to find inspiration.\nTravel the city until all the insprirations have been found then get back to UIC as fast as possible.'
line = ("----------------------------------\n")
last_inpiration_msg = "YOU FOUND THE LAST INSPIRATION!!!\nNow get back to UIC!"
win_msg = line + "|   Congrats - You Won the Game.    |\n|   (Checkout your game stats)      |\n" + line

# Lists for logging locations and inspirations
found_inspirations = []  # keep a list of inspiration locations visited
location_log = []  # keep a log of all locations visited

# Variable setup - suggested variables for holding game state -- you will need to make more as part of the project
menu_choice = ""  # string to hold current main menu choice
current_loc = 'uic'  # string to hold the current location (game starts at uic)

# Milestone 1: Main Menu

print(welcome_msg)

# Main loop function
gameChoices = ["A", "P", "D", "Q"]
continueFlag = True
Flag = ""
location_log.append("uic")
incorrectInput = True

while continueFlag == True:
    for i in main_menu.values():
        print("- " + i)

    userChoice = input("What is your choice? ")

    while userChoice not in gameChoices:
        userChoice = input("Invalid input. Please try again: ")

    # Quit Function
    if userChoice == "Q":
        continueFlag = False
        print("\n" + "Your choice: (Q)uit.")
        print("\n" + "Goodbye!")

    # About Game Function
    elif userChoice == "A":
        print("\n" + "Your choice: (A)bout the game." + "\n")
        print(welcome_msg)
        print(about_msg)
        continueFlag = True

    # Play Game Function
    # Milestone 2: Game Loop
    elif userChoice == "P":

        print("\n" + "Your choice: (P)lay Chicago Explorers!" + "\n")
        GamePlay = True
        if current_loc == "return":
            current_loc = Flag

        # GameLoop Function
        while GamePlay == True:

            nextLocation = current_loc

            if current_loc in locations_map:
                print(line)
                print(f"You are currently at {current_loc}.\n")

                if (current_loc not in found_inspirations) and (current_loc in inspirations):
                    found_inspirations.append(current_loc)
                    print(line)
                    print(f"Congrats! You found an inspiration!\n{inspirations[current_loc]}\n")

                    if len(found_inspirations) == len(inspirations.keys()):
                        print(last_inpiration_msg)

                    print(line)

                print(f"Where would you like to go next?\n")

                validLocations = locations_map[current_loc]
                for places in validLocations:
                    print("-", places)
                print("- (return) to main menu)")
                current_loc = input("Enter next location (or 'return'): ")

                while current_loc not in validLocations and current_loc != "return":
                    current_loc = input("Try again: ")

                if current_loc in locations_map:
                    location_log.append(current_loc)

                uniqueLocations = set(location_log)

                Flag = nextLocation

            elif current_loc == "return":
                GamePlay = False

            while (current_loc not in locations_map) and (current_loc != "return"):
                current_loc = input("Try again: ")
                location_log.append(current_loc)

            if (len(found_inspirations) == 3) and (current_loc == "uic"):
                print(win_msg)
                GamePlay = False

    # Milestone 4: Display Game Stats
    elif userChoice == "D":

        print("\n" + "Your choice: (D)isplay game stats." + "\n" + "\n" + line)
        print(f"GAME STATS:\n")

        # Location Visit Log (Total locations + duplicates!)
        print(f"Location visit log: {len(location_log)} total hops")
        print(f"Locations: {location_log}\n")

        # Unique Locations Visited (No duplicates!)
        print(f"Unique Locations Visited: {len(uniqueLocations)}")
        print(f"Locations: {uniqueLocations}\n")

        # Inspirations!
        print(f"Inspirations found: {len(found_inspirations)}")
        for inspos in found_inspirations:
            print(f"- {inspos}")
        print(line)
