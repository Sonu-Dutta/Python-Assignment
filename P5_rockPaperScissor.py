import random

while True:
    user_input = input("Enter a choice  r / p / s (rock, paper, scissors): ")
    choices = ["r", "p", "s"]
    computer_choice = random.choice(choices)
    print(f"\nYou chose {user_input}, computer chose {computer_choice}.\n")

    if user_input == computer_choice:
        print(f"Both players selected {user_input}. It's a tie!")
    elif user_input == "r":
        if computer_choice == "s":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_input == "p":
        if computer_choice == "r":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_input == "s":
        if computer_choice == "p":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (yes/no): ")
    if play_again.lower() != "yes":
        break