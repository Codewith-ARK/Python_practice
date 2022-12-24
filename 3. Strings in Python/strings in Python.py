print("What are Strings?")
print("Lorem ipsum, dolor sit amet consectetur adipisicing elit. Cupiditate rem dolorum quisquam, ut ipsa esse aliquam. Nisi nulla officia praesentium.")

print("[] Create a Mad Libs Story")
print("[] Search a word in a text")

# creates a story based on the input provided by the user
def madLibs():
    print("What is a Mad Lib?")
    print("Lorem ipsum, dolor sit amet consectetur adipisicing elit. Cupiditate rem dolorum quisquam, ut ipsa esse aliquam. Nisi nulla officia praesentium.")
    name = input("Enter a name: ")
    object = input("Random Object: ")
    city = input("Enter name of a City: ")
    favDish = input("Enter favourite Dish: ")
    animal = input("Enter name of an Animal: ")

    print(name + "was a mighty " + favDish + " He would stomp around " + city + " with a loud" + object + "!" + " The other dinosours thought he was good at hunting " + animal + ".")

# Searches a word in a given text
def Search():
    search = input("Enter a SEARCH TERM: ")