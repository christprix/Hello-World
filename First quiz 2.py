print("Hello! Welcome to my first quiz!")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("Ok. Let's begin!")
score = 0
answer = input ("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input ("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input ("What is the meaning of life? ")
if answer.lower() == "42":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input ("Are you back? *hint babayaga ")
if answer.lower() == "yeah I'm thinking I'm back":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("You got " + str((score / 4) * 100) + "questions correct!")

if score == 4:
    print("You're a genius!")