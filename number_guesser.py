import random
# a = int(input("Type a number "))
a = input("Type a number ")
if a.isdigit():
    a = int(a)
    if a < 0:
        print("Type a positive number next time")
        quit()
else:
    print("Type number next time")
    quit()

times = 0

r = random.randint(0,a)
while True:
    # guess = int(input("Make guess "))
    guess = input("Make guess ")
    times +=1
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Type a number again")
        quit()
        
    if guess == r:
        print("You got it")
        break
    elif guess >= r:
        print("You were above the number ")
    elif guess <= r:
        print("You were below the number")
    else:
        print("Try again")

print("So all the times you tried again is ", times)
