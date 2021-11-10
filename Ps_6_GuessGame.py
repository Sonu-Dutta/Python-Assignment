import random

def guessGame(a1, b1, original_no):
    guess = int(input(f"Guess the number between {a1} and {b1}\n"))
    nguess = 1
    while guess != original_no:
        if guess< original_no:
            guess = int(input(f"Enter a bigger number\n"))
            nguess += 1
        else: 
            guess = int(input(f"Enter a smaller number\n"))   
            nguess += 1

    print(f"You guessed the number in {nguess} guesses\n")
    return nguess


if __name__ == "__main__":
    a = int(input("Enter the starting number: \n"))    
    b = int(input("Enter the ending number: \n"))
    original_no_1 = random.randint(a, b)  
    print("Player 1's turn\n")
    g1 = guessGame(a, b, original_no_1 )
    print("Player 2's turn\n")
    original_no_2 = random.randint(a, b)  
    g2 = guessGame(a, b, original_no_2)

    if g1 < g2:
        print("Player_1 won the match!\n")

    elif g1 > g2:
        print("Player_2 won the match!\n")    
    
    else:
        print("Its a Tie!\n")
    
    print(f"The number for player_1 : {original_no_1 }\n\t   for player_2 : {original_no_2}")