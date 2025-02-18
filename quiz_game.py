print("welcome to my computer quiz")

playing = input("Do y want to play?yes/no ")

if playing.lower() != "yes":
    quit()
print("ok, let's start")

score = 0

answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct")
    score +=1
else:
    print("incorrect")

answer = input("what does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("correct")
    score +=1
else:
    print("incorrect")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("correct")
    score +=1
else:
    print("incorrect")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("correct")
    score +=1
else:
    print("incorrect")

answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct")
    score +=1
else:
    print("incorrect")

answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct")
    score +=1
else:
    print("incorrect")
print("Y got: " + str(score) + "question correct ")
print("Y got: " + str((score/4) * 100) + "%")