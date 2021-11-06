# Snake water gun

import random
lst = ['s','w','g']

chance = 3
no_of_chance = 0
computer_point = 0
human_point = 0

print(" \t \t \t \t Snake,Water,Gun Game\n \n")
print("s for snake \nw for water \ng for gun \n")

while no_of_chance < chance:
    _input = input('Snake, Water, Gun:')
    _random = random.choice(lst)

    if _input == _random:
        print(f"Your guess {_input} and computer guess is {_random} \n")
        print("Tie Both 0 point to each \n ")
        
    elif _input == "s" and _random == "g":
        computer_point = computer_point + 1
        print(f"Your guess {_input} and computer guess is {_random} \n")
        print("Computer wins 1 point \n")
        print(f"Computer_point is {computer_point} and your point is {human_point} \n ")

    elif _input == "s" and _random == "w":
        human_point = human_point + 1
        print(f"Your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"Computer_point is {computer_point} and your point is {human_point} \n")

    elif _input == "w" and _random == "s":
        computer_point = computer_point + 1
        print(f"Your guess {_input} and computer guess is {_random} \n")
        print("Computer wins 1 point \n")
        print(f"Computer_point is {computer_point} and your point is {human_point} \n ")

    elif _input == "w" and _random == "g":
        human_point = human_point + 1
        print(f"Your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"Computer_point is {computer_point} and your point is {human_point} \n")

    elif _input == "g" and _random == "s":
        human_point = human_point + 1
        print(f"Your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"Computer_point is {computer_point} and your point is {human_point} \n")


    elif _input == "g" and _random == "w":
        computer_point = computer_point + 1
        print(f"Your guess {_input} and computer guess is {_random} \n")
        print("Computer wins 1 point \n")
        print(f"Computer_point is {computer_point} and your point is {human_point} \n ")

    else:
        print("Wrong input, Please enter valid input !!! \n")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} chances. \n")

print("Game over")

if computer_point==human_point:
    print("Tie")

elif computer_point > human_point:
    print("Computer wins and you loose")

else:
    print("You win and computer loose")

print(f"Your point is {human_point} and computer point is {computer_point}")

