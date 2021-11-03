import random

rNumberStart = 0
rNumberCap = 10 + 1
rNumber = random.randrange(11)

plays = 3
while plays > 0:

    # player input
    answer = input(
        f"Please pick a number between {rNumberStart} and {rNumberCap - 1} ")

    # if input isn't a digit
    if not answer.isdigit():
        print("Please type in a number...")

    # else if the number isn't in the specified range
    elif int(answer) not in list(range(rNumberStart, rNumberCap)):
        print(
            f"Please type a number within the range of {rNumberStart} and {rNumberCap}")

    # start the game
    else:
        answer = int(answer)
        if answer == rNumber:
            print(f"\nYou are correct!! The answer was {rNumber}!\n")
            plays = True
            break
        elif answer > rNumber:
            print("Try going lower...")
            plays -= 1
        elif answer < rNumber:
            print("Trying going higher...")
            plays -= 1
        else:
            print("Guess again!")
            plays -= 1

if plays == True:
    print("=" * 25)
    print("You won!")
    print("=" * 25)
else:
    print("You lost! Try again next time!")

print("\nThanks for playing!")
