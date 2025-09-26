print("Welcome to the meh-thematical calculator or something...")

def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
def exp(a, b):
    return a ** b
first = True
going = True
while going:

    if first == False:
        quit = input("Are you going to finally leave me alone? (y/n): ")
        if quit == "y":
            print("About time.")
            going = False
            break
    first = False

    choice = input("Ugh, what do you want this time? \n 1: add \n 2: subtract \n 3: multiply \n 4: divide \n 5: exponent\n 6: help me I'm stupid and can't do math! \n 7: exit \n >")
    if choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5":
        try:
            a = float(input("Enter a number, or dont: "))
            b = float(input("Enter another number, actually please dont: "))
        except:
            print("This is math, you gotta put in a number.")
            continue

    if choice == "1":
        print(add(a, b))
    elif choice == "2":
        print(sub(a, b))
    elif choice == "3":
        print(mul(a, b))
    elif choice == "4":
        if b == 0:
            print("You know you can't divide by zero, right? Try again.")
            continue
        print(div(a, b))
    elif choice == "5":
        print(exp(a, b))
    elif choice == "6":
        print("So you're really too stupid to put some numbers into a calculator, huh. \n ---Addition--- \n a + b \n ---Subtraction--- \n a - b \n ---multiplication--- \n a x b \n ---division--- \n a / b \n You can't divide by zero. \n ---exponent--- \n a ^ b")
    elif choice == "7":
        print("Finally.")
        break
    else:
        print("You really can't just type a number 0 through 7 and hit enter? What a loser.")
        continue