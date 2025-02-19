a = input("What is the master password? ")

def view ():
    pass



def add():
    acc = input("Account Name: ")
    passw = input("Password: ")
    with open('password.txt', 'a', )


while True:
    mode = input("Would you like to add a new password or view existing ones? (view/add) or press Q to quit? ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invalid mode")
        continue