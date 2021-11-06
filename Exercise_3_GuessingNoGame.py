# You have to build a "Number Guessing Game," in which a winning number is set to some integer value. 
# The Program should take input from the user, and if the entered number is less than the winning number,
# a message should display that the number is smaller and vice versa.

# 1. The number of guesses should be limited.
# 2. Print the number of guesses left.
# 3. Print the number of guesses he took to win the game.
# 4. “Game Over” message should display if the number of guesses becomes 0.
import random
random_no=random.randint(0,10)
number_of_guesses=1
print("Number of guesses is limited to only 5 times: ")
while (number_of_guesses<=5):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<random_no:
        print("The entered number is less than the winning number.\n")
    elif guess_number>random_no:
        print("The entered number is greater than the winning number.\n ")
    else:
        print("You won !!!\n")
        print("Number of guesses you took to finish : ",number_of_guesses)
        break
    print("Number of guesses left : ",5-number_of_guesses)
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>5):
    print("Game Over")