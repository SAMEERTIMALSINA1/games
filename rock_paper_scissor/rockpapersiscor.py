import random

def computer_play():
    result = random.choice(play_items)
    return result

def user_play():
    user_input = input("Enter rock or paper or scissor: ")
    return user_input

def checker(computer_choice,user_choice):
    if computer_choice == user_choice:
        return "Draw"
    elif computer_choice=="rock" and user_choice=="scissor":
        return "You Lose!"
    elif computer_choice=="paper" and user_choice=="rock":
        return "You Lose!"
    elif computer_choice=="scissor" and user_choice=="paper":
        return "You Lose!"
    else:
        return "You Win!"
    
play_items=["rock","paper","scissor"]

# variable assignment to function
user_choice = user_play()
computer_choice = computer_play()

print(computer_choice)

print(checker(computer_choice,user_choice))