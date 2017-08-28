# multipication-game.py

from time import *
import random

def countdown():
    ''' Counts down to new game'''
    print("Starting in")
    print("3...")
    sleep(1)
    print("2...")
    sleep(1)
    print("1...")
    sleep(1)
    print("GO!")

def generate_new_num(my_min=1, my_max=10):
    '''Returns a random integer between the two values, with the defaults set at 1 and 10.'''
    return random.randint(my_min, my_max)

def print_nums(my_first, my_second):
    '''Prints first and second numbers for the player'''
    print(my_first, "x", my_second)

def new_round():
    '''Starts a new round with new numbers'''
    first_num = generate_new_num()
    second_num = generate_new_num()
    solution = first_num * second_num
    print_nums(first_num, second_num)
    player_answer = int(input(": "))
    if player_answer == solution:
        print("Correct!")
        return True
    else:
        print("Wrong!")
        return False

def new_game():
    counter = 3
    score = 0
    countdown()
    while counter > 0:
        game = new_round()
        if game:
            score += 1
        counter -= 1
    
    print("Game over! Your final score is:", score)



if __name__ == "__main__":
    #countdown()
    new_game()
