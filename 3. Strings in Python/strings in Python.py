import os

# creates a story based on the input provided by the user
def madLibs():
    print("What is a Mad Lib?")
    print("Lorem ipsum, dolor sit amet consectetur adipisicing elit. Cupiditate rem dolorum quisquam, ut ipsa esse aliquam. Nisi nulla officia praesentium.")
    name = input("\n\tEnter a name: ").upper()
    object = input("\tRandom Object: ").upper()
    city = input("\tEnter name of a City: ").upper()
    favDish = input("\tEnter favourite Dish: ").upper()
    animal = input("\tEnter name of an Animal: ").upper()

    print(name + " was a mighty " + favDish + " He would stomp around " + city + " with a loud " + object + "!" + " The other dinosours thought he was good at hunting " + animal + ".")

# Searches a word in a given text
def Search():
    search = input("Enter a SEARCH TERM: ")

### MAIN METHOD
os.system("cls")
os.system("color 2")
print("\t\t---Working with STRING---")
print("\n\tWhat are Strings?")
print("\t- Lorem ipsum, dolor sit amet consectetur adipisicing elit. Cupiditate rem dolorum quisquam, \n\t  ut ipsa esse aliquam. Nisi nulla officia praesentium.")

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