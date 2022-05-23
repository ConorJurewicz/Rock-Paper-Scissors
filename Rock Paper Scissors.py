import random


selection = ['rock','paper','scissors']

while True:

    robot_choice = random.choice(selection)
    user_choice = input('Rock Paper Scissors, shoot! ').lower()

    while user_choice not in selection:
        user_choice = input('Spelling error, try again. ').lower()
        
    if user_choice == robot_choice:
        print("The robot chose ", robot_choice)
        print("So, you tied.")

    elif user_choice == "rock":
        if robot_choice == "paper":
            print("The robot chose ", robot_choice)
            print("So, you lose.")
        if robot_choice == "scissors":
            print("The robot chose ", robot_choice)
            print("So, you win!")

    elif user_choice == "scissors":
        if robot_choice == "rock":
            print("The robot chose ", robot_choice)
            print("So, you lose.")
        if robot_choice == "paper":
            print("The robot chose ", robot_choice)
            print("So, you win!")
            
    elif user_choice == "paper":
        if robot_choice == "scissors":
            print("The robot chose ", robot_choice)
            print("So, you lose.")
        if robot_choice == "rock":
            print("The robot chose ", robot_choice)
            print("So, you win!")