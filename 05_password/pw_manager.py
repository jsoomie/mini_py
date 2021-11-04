
from cryptography.fernet import Fernet
# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


exit = ["exit", "q", "quit"]
key_password = input("What is the KEY password? ")
key = load_key() + key_password.encode()
fer = Fernet(key)


def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split("|")
            print(
                f"User: {user} || Password: {fer.decrypt(password.encode()).decode()}")


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


active = True
while active == True:
    mode = input("Add or view password? Q to quit. (view / add)  ").lower()
    if mode in exit:
        break

    if mode == "view":
        view()
        continue
    elif mode == "add":
        add()
        continue
    else:
        print("Invalid mode")
        continue
