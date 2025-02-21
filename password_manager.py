# Dùng mã khóa để mã hóa mật khẩu.
# Lưu mật khẩu đã mã hóa vào file.
# Khi cần sử dụng, dùng cùng mã khóa để giải mã.
# Load mã khoá để mã hoá và giải mã


from cryptography.fernet import Fernet #this model allows you to encrypt the data 
import os

# create key (only run once )
def generate_key():
    if os.path.exists("key.key"):
        print("Key already exists. Skipping key generation.")
        return 
    
    key = Fernet.generate_key()
    with open("key.key", "wb") as f:
        key = input("Enter key:")
        f.write(key)
    print("New key has been generated and saved. It can't be changed")

generate_key()

#load key from file key.key 
def load_key():
    try:
        with open("key.key", "rb") as load_f:
            return load_f.read()
    except FileNotFoundError:
        print("File not found. Gennerate a key first")
        exit()

a = input("What is the master password? ")

key = load_key() 

if a.encode() != key:
    print("Error: Incorrect master key!")
    exit()

fer = Fernet(key)

def view ():
    with open('password.txt', 'r') as read_f:
        for line in read_f.readlines():
            acc, passw = line.strip().split("|")
            decrypted_passw = fer.decrypt(passw.encode()).decode() # Decrypt the password before showing to the user
            print("Account :", acc)
            print("Password: ", decrypted_passw , "\n")  


def add():
    acc = input("Account Name: ")
    passw = input("Password: ")

    # file = open('ps.txt','a')
    # file.close()
    with open('password.txt', 'a') as f:
        f.write(acc + "|" + fer.encrypt(passw.encode()).decode() + "\n")        


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