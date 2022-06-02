import random

def rps():
    print("Hello! Welcome to Rock, Paper, Scissors. To play the game pick an option between R, P, or S")

    RPS_list= ["R", "P", "S"]


    comp_turn=(random.choice(RPS_list))
    user_turn=input("R, P, or S?")

    while user_turn.upper() not in RPS_list:
        print("Error: Invalid input! You have not entered R, P, or S, try again.")
        user_turn= input("R, P, or S?")

  
    if comp_turn.upper() == user_turn.upper():
        print(f'Player({user_turn}):CPU({comp_turn})')
        print("It's a draw!")
        rps()
    elif comp_turn.upper()== "R":
        if user_turn.upper()=="P":
            print(f'Player({user_turn}):CPU({comp_turn})')
            print("You Win!")
        else:
            print(f'Player({user_turn}):CPU({comp_turn})')
            print("Computer Wins!")

    elif comp_turn.upper()=="S":
        if user_turn.upper()=="R":
            print(f'Player({user_turn}):CPU({comp_turn})')
            print("You Win!")
        else:
            print(f'Player({user_turn}):CPU({comp_turn})')
            print("Computer Wins!")
    elif comp_turn.upper()=="P":
        if  user_turn.upper()=="S":
            print(f'Player({user_turn}):CPU({comp_turn})')
            print("You Win!")
        else:
            print(f'Player({user_turn}):CPU({comp_turn})')
            print("Computer Wins!")
    else:
        print("Error:Invalid input! You have not entered R, P, or S, try again.")

rps()