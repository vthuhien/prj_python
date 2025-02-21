from cryptography.fernet import Fernet #this model allows you to encrypt the text 

# if you enter the wrong password, it can't decrypt the text

# # make key for us
# def main_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_f: #use wb for binary file
#         key_f.write(key)


def load_key():
    with open("key.key", "rb") as load_f:
        check_key = load_f.read()
    return check_key

a = input("What is the master password? ")
key = load_key() + a.encode() #convert a from string to bytes for encrypting
fer = Fernet(key)

def view ():
    with open('password.txt', 'r') as read_f:
        for line in read_f.readlines():
            data = line.rstrip()
            acc, passw = data.split("|")
            print("Account :", acc)
            print("Password: ", str(fer.encrypt(passw.encode())), "\n")  #encrypt data with Fernet and convert it into a string for easy file entry
            # if the user enters the correct password, the password will be decrypted


def add():
    acc = input("Account Name: ")
    passw = input("Password: ")

    # file = open('ps.txt','a')
    # file.close()
    with open('password.txt', 'a') as f:
        f.write(acc + "|" + str(fer.encrypt(passw.encode())) + "\n")
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