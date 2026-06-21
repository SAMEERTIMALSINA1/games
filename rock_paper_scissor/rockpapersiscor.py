import random

def computer_play():
    result = random.choice(play_items)
    return result

def user_play():
    user_input = input("Enter rock or paper or scissor: ")
    return user_input

def checker():
    if computer_play == user_play:
        return "Draw"
    elif computer_play=="rock" and user_play=="scissor":
        return "You Lose!"
    elif computer_play=="paper" and user_play=="rock":
        return "You Lose!"
    elif computer_play=="scissor" and user_play=="paper":
        return "You Lose!"
    else:
        return "You Win!"
    
play_items=["rock","paper","scissor"]

# variable assignment to function
user_play = user_play()
computer_play = computer_play()

print(computer_play)

print(checker())