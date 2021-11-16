#using import module:

import random   
winning_number = random.randint(1,10)
guess = 1
number = int(input("Guess a number between 1 to 10 : "))
game_over = False
while not game_over:
    if number == winning_number:
        print(f"You win ! and you guessed this number is {guess} times")
        game_over = True
    else:
        if number < winning_number:
            print("Too low")
            guess += 1
            number = int(input("Please guess again : "))
        else:
            print("too high")
            guess += 1
            number = int(input("Please guess again : "))
