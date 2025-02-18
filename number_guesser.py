import random
# a = input()
# b = a.isdigit()
# print(b)

top_of_range = input("Type a number you want to random: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range) #use for converting output to int
    
    if top_of_range <= 0:
        print("Pls type of number larger than 0 next time.")
        quit()
else:
    print("Pls type of number next time.")
    quit()

# r = random.randrange(0, 11) #include nagetive number
r = random.randint(0,top_of_range)
total_guess = 0

while True:
    user_guess = input("Type a number you guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        
        if user_guess <= 0:
            print("Pls type of number larger than 0 next time.")
            quit()
    else: 
        print("Pls type of number next time.")
        continue #allow users re-enter when they enter the wrong input
    if user_guess == r:
        print("wow, that's correct. Y got it")
        break
    else: 
        # print("oh no, it's wrong. It's ", r) 

        if user_guess > r:
            print("Y were above the number")
        else:
            print("Y were below the number")
        total_guess += 1
        # break      #if the user makes a wrong guess, it still run
    
print("The total number of time you guessed is", total_guess)


