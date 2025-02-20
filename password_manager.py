from cryptography.fernet import Fernet #this model allows you to encrypt text 

a = input("What is the master password? ")
# if you enter the wrong pass, the decrypted text will be incorrect

# make key for us
def main_key():
    key = Fernet.generate_key()
    with open("key.key", "wb"): #use wb for binary file
        pass
def view ():
    with open('password.txt', 'r') as read_f:
        for line in read_f.readlines():
            data = line.rstrip()
            acc, passw = data.split("|")
            print("Account :", acc)
            print("Password: ", passw, "\n")


def add():
    acc = input("Account Name: ")
    passw = input("Password: ")

    # file = open('ps.txt','a')
    # file.close()
    with open('password.txt', 'a') as f:
        f.write(acc + "|" + passw + "\n")
        #pip install cryptography for password


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