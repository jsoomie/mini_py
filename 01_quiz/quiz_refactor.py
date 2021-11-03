questions = {
    "What does CPU stand for?": "central processing unit",
    "What does GPU stand for?": "graphics processing unit",
    "What does RAM stand for?": "random access memory",
    "What does PSU stand for?": "power supply unit"
}

score = 0

print("\n\nWelcome to the computer quiz!\n\n")
playing = input("Would you like to play? (y/n) ").lower()
if playing != "yes" or playing != "y":
    quit()

for question in questions:
    answer = questions[question]
    userInput = input(f"{question} ").lower()
    if userInput == answer:
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")
