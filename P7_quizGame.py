def check(guess, answer): 
    global score 
    still_guessing = True 
    attempt = 0 
    while still_guessing and attempt < 3: 
        if guess.lower() == answer.lower(): 
            print("Correct Answer !!!") 
            score = score + 1 
            still_guessing = False 
        
        else: 
            if attempt < 2: 
                guess = input("Sorry Wrong Answer, try again!") 
            attempt = attempt + 1 
    if attempt == 3: 
                print("The Correct answer is ",answer ) 
score = 0
print("Guess the Animal")
guess1 = input("Which animal has 3 hearts? ")
check(guess1, "octopus")
guess2 = input("Which animal has blue blood? ")
check(guess2, "spider")
guess3 = input("Which is the second smartest animal on earth after human? ")
check(guess3, "dolphin")
print("Your Score is "+ str(score))
