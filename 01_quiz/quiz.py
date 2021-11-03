print("\n\nWelcome to the computer quiz\n\n")

playing = input("\nDo you wish to play: ").lower()

if playing != "yes":
    quit()

print("\nLets play!\n\n")

score = 0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("=" * 25)

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("=" * 25)

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("=" * 25)

answer = input("What does PSU stand for? ").lower()
if answer == "power supply unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("=" * 25)

print(f"Your score is: {score} out of 4")
print(f"You got {(score/4) * 100} %")
