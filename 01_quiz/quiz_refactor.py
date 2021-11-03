questions = {
    "What does CPU stand for?": "central processing unit",
    "What does GPU stand for?": "graphics processing unit",
    "What does RAM stand for?": "random access memory",
    "What does PSU stand for?": "power supply unit"
}

print("\n\nWelcome to the computer quiz!\n\n")
playing = input("Would you like to play? (y/n) ").lower()
if playing != "yes" and playing != "y":
    quit()
else:
    playing = True

while playing == True:
    score = 0

    for question in questions:
        answer = questions[question]
        userInput = input(f"{question} ").lower()
        if userInput == answer:
            print("Correct!\n")
            score += 1
        elif userInput == "quit" or userInput == "q":
            print("Exiting program........")
            playing = False
            break
        else:
            print("Incorrect!\n")
    if playing == False:
        break
    print(f"Your score is: {score} out {len(questions)}")
    print(f"That's {(score/ 4 * 100)} %!")
    playing = False

print("\nThanks for playing!\n")
quit()
