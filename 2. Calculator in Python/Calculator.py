import os
count = 1
while True:
    # Clearing the Screen
    os.system('cls')

    print("Iteration Number: ", count, end="\n\n")
    count += 1

    a = float(input("\tA: ")) # provide value for variable A
    b = float(input("\tB: ")) # provide value for variable B

    # End condition for the LOOP
    if(a == 69420):
        print("\tEXITING Loop")
        break

    op = input("Enter the operation: ")

    if(op == '+'):
        print("Answer: ",(a + b))
    elif(op == '-'):
        print("Answer: ",(a + b))
    elif(op == '*'):
        print("Answer: ",(a + b))
    elif(op == '/'):
        print("Answer: ",(a + b))
    else:
        print("WRONG input!")

    #Making the Program wait before starting the Loop Again
    wait = input("\nPress ENTER to continue...")