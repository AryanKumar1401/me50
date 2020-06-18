user_1 = input("Enter your name: ")
user_2 = input("Player 2: ")  
ans_1 = str(input("Does player 1 choose rock, paper or scissors? "))
ans_2 = str(input("And what does Player 2 choose? "))

def compare(ans_1, ans_2):
    if ans_1 == ans_2:
        return ("It's  tie!")
    elif ans_1 == 'rock':
        if ans_2 == 'scissors':
            return ("Player 1 wins!")
        elif ans_2 == 'paper': 
            return ("Player 2 wins!") 

    elif ans_1 == 'paper':
        if ans_2 == 'scissors':
            return ("Player 2 wins!")
        elif ans_2 == 'rock':
            return ("Player 1 wins!")

    elif ans_1 == 'scissors':
        if ans_2 == 'rock':
            return ("{user_1} ")      
