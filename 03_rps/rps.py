import random

userWins = 0
compWins = 0
options = ["rock", "paper", "scissors"]
while True:
    userInput = input(f"Type {', '.join(options) } or Q to quit. ").lower()
    if userInput == "q":
        break

    if userInput not in options:
        continue

    compPick = options[random.randint(0, 2)]
    print(f"Computer picked {compPick}.")

    def display(outcome):
        if outcome == "win":
            print("\nYOU WON")
        elif outcome == "lost":
            print("\nYOU LOST")
        else:
            print("\nYou tied...")
        print(f"\nCurrent score: YOU: {userWins} - COMP: {compWins}\n")

    if userInput == "rock" and compPick == "scissors":
        userWins += 1
        display("win")
        continue
    elif userInput == "paper" and compPick == "rock":
        userWins += 1
        display("win")
        continue
    elif userInput == "scissors" and compPick == "rock":
        userWins += 1
        display("win")
        continue
    elif userInput == compPick:
        display("tie")
    else:
        compWins += 1
        display("lost")

if userWins > compWins:
    print("\nYOU ARE THE WINNER!\n")
elif userWins == compWins:
    print("\nIt's a tie!\n")
else:
    print("\nYOU LOST\n")

print("Thanks for playing!")
