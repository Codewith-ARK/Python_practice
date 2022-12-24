import os

# creates a story based on the input provided by the user
def madLibs():
    
    os.system("cls")
    os.system("color 3")

    print("\t\t---Create a Mad Libs---")
    print("\nWhat is a Mad Lib?")
    print("- Lorem ipsum, dolor sit amet consectetur adipisicing elit. Cupiditate rem dolorum quisquam,\n ut ipsa esse aliquam. Nisi nulla officia praesentium.")
    
    print("\n\n\tEnter the details to generate a Mad-Libs: ")
    name = input("\t- Any name: ").upper()
    object = input("\t- Random Object: ").upper()
    city = input("\t- Name of a City: ").upper()
    favDish = input("\t- Favourite Dish: ").upper()
    animal = input("\t- Name of an Animal: ").upper()

    print("\n\t\"" + name + " was a mighty " + favDish + " He would stomp around " + city + " with a loud " + object + "!" + "\n\t\tThe other dinosours thought he was good at hunting " + animal + "\".\n\n")

# Searches a word in a given text
def Search():
    search = input("Enter a SEARCH TERM: ")

### MAIN METHOD
os.system("cls")
os.system("color 2")
print("\t\t---Working with STRING---")
print("\nWhat are Strings?")
print("- Lorem ipsum, dolor sit amet consectetur adipisicing elit. Cupiditate rem dolorum quisquam, \n  ut ipsa esse aliquam. Nisi nulla officia praesentium.")

print("\n\n\t\t\t---MENU---")
print("\n\t\t[1] Create a Mad Libs Story")
print("\t\t[2] Search a word in a text")

while True:
    ans = int(input("Your CHOICE: "))
    match ans:
        case 1:
            madLibs()
            break
        case 2:
            Search()
            break
        case _:
            os.system("color 4")
            print("\t- WRONG INPUT!")