confirmation = {"yes", "y", "ok", "okay", "yup", "yep",
                "yeah", "yea", "okie dokie", "okie", "k", "kk", "correct", "exactly", "confirm"}
rejection = {"no", "n", "nah", "nope", "nuh uh",
             "nuhuh", "not it", "reject", "cancel", "back"}


up = {"u", "up", "north", "n"}
right = {"r", "right", "east", "e"}
down = {"d", "down", "south", "s"}
left = {"l", "left", "west", "w"}


def gameOver():
    print("GAME OVER")


def error(text="Not a valid action"):
    print(text)


def desc(text="Room desc here"):
    print(f"DESC: {text}")


def space():
    print("\n")


def displayDirection():
    direction = input("\nWhich direction do you head to? ").lower()
    if direction in up:
        return "up"
    elif direction in right:
        return "right"
    elif direction in down:
        return "down"
    elif direction in left:
        return "left"
    else:
        return direction


# START
print("Welcome to the adventure!")
introPlay = True


def scene02_woods():
    desc("A dark foggy woodsy area. North is the deep woods. East is the pond. West is the barn.")
    direction = displayDirection()
    if direction == "left":
        print("You head towards the barn.")
        print("The barn explodes as you reach it.")
        print("You die.")
        gameOver()
    elif direction == "right":
        print("You head towards the pond.")
        print("The pond never seems to get closer.")
        print("You feel like you were walking for a very long time.")
        print("You die.")
        gameOver()
    elif direction == "up":
        print("You head deeper into the woods.")
        print("You walk deep into the woods.")
        print("You are lost for who knows how long.")
        print("You die.")
        gameOver()
    elif direction in rejection:
        print("You head back inside the cabin.")
        print("You stay there forever and die.")
        gameOver()


def scene01_left_room():
    print("You head through the left doorway. ")
    print("It's too dark to see anything....")
    confirm = input("Continue forth? (y/n) ").lower()
    if confirm in confirmation:
        space()
        print("With your hand on the left side of the wall, you slowly inch forward towards the darkness.")
        print(
            "After what feels like a few minutes, you feel like you are at the end of the hallway.")
        print("A closed door can be felt and you fumble with the doorknob before finally turning it and stubmling out through the doorway.")
        print(
            "You suddenly find yourself in the middle of the woods. It is dark and foggy."
        )
        print("The pathway leads to 3 different direction.")
        print("You look around to find a barn to your left, a pond to your right and the deep woods to the north")
        scene02_woods()
    elif confirm in rejection:
        space()
        print("You turn back into the room.")
        scene01()
    else:
        error()


def scene01_right_room():
    space()
    print("You head through the right doorway.")
    print("You die")
    gameOver()


def scene01_intro():
    space()
    print("You wake up in a unfamiliar room.")
    print("The room is empty.")
    print("There are two doorways: one to the left and one to the right. Both look like they lead to a dark hallway.")
    scene01()


def scene01():
    space()
    desc("The room you first started in. It is empty...\nThere's a doorway to left and right that leads into darkness")
    choice = True
    while choice == True:
        direction = displayDirection()
        if direction == "left":
            scene01_left_room()
            choice = False
        elif direction == "right":
            scene01_right_room()
            choice = False
        else:
            error("There's nothing there...")
            continue


while introPlay == True:
    name = input("Please enter your name: ")
    nameConfirmation = input(f"Your name is {name}, correct? (y/n) ").lower()
    if nameConfirmation in confirmation:
        greeting = f"Welcome, {name}, to the adventure of a lifetime!"
        print(greeting)
        print("=" * len(greeting) + "\n")
        scene01_intro()
        introPlay = False
    else:
        continue
