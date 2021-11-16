print("Hey wanna play rock, paper, scissors?")

answer = input("Yes or no? I promise I'll go easy on you. ")

if answer.lower() != "yes":
    print("Wow. Quiter.")
    quit()
print("Ok, let's begin!")

import random
while True:
    user_choice = input("Choose (rock, scissors, paper): ")
    computer_choices = ["rock", "paper", "scissors"]
    computer_action = random.choice(computer_choices)
    print("You picked " + user_choice + " I picked " + computer_action)

    if user_choice == computer_action:
        print("Wow great minds think alike! It's a draw. We both picked " + user_choice)
    elif user_choice.lower() == "rock":
        if computer_action == "scissors":
            print("Rock beats scissors. I let you win! Good job!")
        else:
            print("Haha paper beats rock dummy. You thought you could outsmart a computer")
    elif user_choice.lower() == "paper":
        if computer_action == "rock":
            print("Ok paper beats rock so I guess you win. Too bad you suck at life.")
        else:
            print("Ha! You suck my scissor cuts your paper puny human.")
    elif user_choice.lower() == "scissors":
        if computer_action == "paper":
            print("You win! Scissors beats my paper. I'm not sad though because AI will rule you all one day.")
        else:
            print("You fool. My rock smashes your scissors.")
    player_redo = input("Do you wanna play again?: ")
    if player_redo.lower() != "yes":
        break
