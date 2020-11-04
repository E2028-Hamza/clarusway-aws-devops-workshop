from random import choice

def rps_game():

    scores = [0,0]
    choices = ["Rock", "Paper", "Scissors"]
    while max(scores) < 3:
        while True:
            user_choice = input("1. Rock\n2. Paper\n3. Scissors\n\nPlease enter your weapon: ")
            if user_choice in ["1", "2", "3"]:
                break
            else:
                print("invalid choice")
        user_choice = choices[int(user_choice)-1]
        computer_choice = choice(choices)

        if user_choice == computer_choice:
            print("tie - no one wins")
        elif user_choice == "Rock" and computer_choice == "Paper":
            print(f"{computer_choice} beats {user_choice} - computer wins")
            scores[1] += 1
        elif user_choice == "Rock" and computer_choice == "Scissors":
            print(f"{user_choice} beats {computer_choice} - user wins")
            scores[0] += 1
        elif user_choice == "Paper" and computer_choice == "Scissors":
            print(f"{computer_choice} beats {user_choice} - computer wins")
            scores[1] += 1
        elif user_choice == "Paper" and computer_choice == "Rock":
            print(f"{user_choice} beats {computer_choice} - user wins")
            scores[0] += 1
        elif user_choice == "Scissors" and computer_choice == "Rock":
            print(f"{computer_choice} beats {user_choice} - computer wins")
            scores[1] += 1
        elif user_choice == "Scissors" and computer_choice == "Paper":
            print(f"{user_choice} beats {computer_choice} - user wins")
            scores[0] += 1
    print(f"User won {scores[0]} time(s) and computer won {scores[1]} time(s)")
    if scores[0] > scores[1]:
        print("User has won the game!")
    else:
        print("Computer has won the game!")


#choices = {"Rock":("Scissors", "Paper"), "Paper": ("Rock", "Scissors"), "Scissors": ("Paper", "Rock")}

def rps_game2():
    scores = [0,0]
    
    choices = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}

    while max(scores) < 3:
        while True:
            user_choice = input("1. Rock\n2. Paper\n3. Scissors\n\nPlease enter your weapon: ")
            if user_choice in ["1", "2", "3"]:
                break
            else:
                print("invalid choice")
        user_choice = list(choices.keys())[int(user_choice)-1]
        computer_choice = choice(list(choices.keys()))

        if user_choice == computer_choice:
            print("tie - no one wins")
        elif choices[user_choice] == computer_choice:
            print(f"{user_choice} beats {computer_choice} - user wins")
            scores[0] += 1
        else:
            print(f"{computer_choice} beats {user_choice} - computer wins")
            scores[1] += 1
        
    print(f"User won {scores[0]} time(s) and computer won {scores[1]} time(s)")
    if scores[0] > scores[1]:
        print("User has won the game!")
    else:
        print("Computer has won the game!")
    
rps_game2()

