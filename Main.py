import pyfiglet
from random import randint

print("")
print(pyfiglet.figlet_format("No. Guessing Game", justify="center", width=110))
print(pyfiglet.figlet_format("Created By Shinjan", justify="center", width=110))

guess = 0
random_num = randint(1,100)

while True:
    
    try:

        print("")
        user_input = int(input("Guess The Number: "))

        if user_input > random_num:
            print("")
            print("You were above the number!")
            guess = guess + 1

        elif user_input < random_num:
            print("")
            print("You were below the number!")
            guess = guess + 1

        elif user_input == random_num:
            guess = guess + 1
            print("")
            print(pyfiglet.figlet_format("Congratulations!", width=110))
            print("")
            print("You Got The Number!")
            print("")
            print(f"You took {int(guess)} Guesses!")
            print("")
            break

    except ValueError:
        print("")
        print("Please Enter A Digit! :/")
        continue