import os

places = []
actions = []
items = []

for dirname, subdirs, files in os.walk('game'):

    if dirname.endswith('actions'):
        for file in files:
            actions.append(file.replace(".txt", ""))

    if dirname.endswith('places'):
        for file in files:
            places.append(file.replace(".txt", ""))

    if dirname.endswith('items'):
        for file in files:
            items.append(file.replace(".txt", ""))

print(places)
print(actions)
print(items)

print()

choice = ""
backpack = []

print("Welcome to the world of adventures!\n")
print("Listed above are places you can go to, things to do, and items to find.\n")

while choice != "quit":

    filename = choice + ".txt"

    if os.path.exists(os.path.join("game", "places", filename)):
        with open(os.path.join("game", "places", filename)) as file:
            print(file.read())
            print()

    elif os.path.exists(os.path.join("game", "actions", filename)):
        with open(os.path.join("game", "actions", filename)) as file:
            print(file.read())
            print()

    elif os.path.exists(os.path.join("game", "items", filename)):
        with open(os.path.join("game", "items", filename)) as file:
            print("You picked up a(n) {}." .format(choice))
            backpack.append(choice)
            print()

    elif choice == "backpack":
        print(backpack)
        print()

    elif choice == "empty":
        for item in backpack:
            backpack.remove(item)
        print("Your backpack is now empty.\n")
        #At this point, my backpack should be empty. However, not ALL items are being removed. Why is that?

    choice = input("""Would you like to 
 a) go to a certain PLACE,
 b) complete an ACTION,
 c) pick up an ITEM, 
 d) seek the contents of your BACKPACK, 
 e) EMPTY your backpack, or
 e) QUIT?\n""")