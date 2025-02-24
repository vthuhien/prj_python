# Dùng mã khóa để mã hóa mật khẩu.
# Lưu mật khẩu đã mã hóa vào file.
# Khi cần sử dụng, dùng cùng mã khóa để giải mã.
# Load mã khoá để mã hoá và giải mã


from cryptography.fernet import Fernet 
import os
import base64
import hashlib

def convert(password: str) -> bytes: #convert entered key into valid Fernet key (32 bytes)
    key = hashlib.sha256(password.encode()).digest() 
    return base64.urlsafe_b64encode(key)

# create key (only run once )
def generate_key():
    if os.path.exists("key.key"):
        print("Key already exists. Skipping key generation.")
        return
    
    password = input("Enter master password: ")
    key = convert(password)

    with open("key.key", "wb") as f:
        f.write(key)
    
    print("Master key has been created!")
#load key from file key.key 
def load_key():
    try:
        with open("key.key", "rb") as load_f:
            return load_f.read()
    except FileNotFoundError:
        print("File not found. Gennerate a key first")
        exit()

generate_key()

a = input("What is the master password? ")

key = convert(a)

stored_key = load_key()

max_tmp = 3
tmp = 0
while tmp < max_tmp:
    tmp +=1
    print(f"You have {max_tmp - tmp} times ")
    a2 = input("Try again: ") 
    key = convert(a2) #update key 
    if key == stored_key:
        break
else:
    print("Error")
    quit()


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

#fjfj