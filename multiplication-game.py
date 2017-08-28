# multipication-game.py

import time
import random
import signal

def countdown():
    ''' Counts down to new game'''
    print("Starting in")
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("GO!")

def generate_new_num(my_min=1, my_max=10):
    '''Returns a random integer between the two values, with the defaults set at 1 and 10.'''
    return random.randint(my_min, my_max)

def player_input(first, second):
    '''Gets player answer and checks if it is an integer.'''
    while True:
        try:
            return int(input(": "))
        except ValueError:
            print("That's not a number!")
            print_nums(first, second)

def print_nums(my_first, my_second):
    '''Prints first and second numbers for the player'''
    print(my_first, "x", my_second)

def new_round():
    '''Starts a new round with new numbers'''
    first_num = generate_new_num()
    second_num = generate_new_num()
    solution = first_num * second_num
    print_nums(first_num, second_num)
    player_answer = player_input(first_num, second_num)
    if player_answer == solution:
        print("Correct!")
        return True
    else:
        print("Wrong!")
        return False

def timeout_handler(signal, frame):
    raise Exception('Time is up!')
signal.signal(signal.SIGALRM, timeout_handler)

def new_game():
    '''Starts a new game.'''
    #start = time.time()
    score = 0
    countdown()
    signal.alarm(10)
    try:
        #while time.time() - start < 20:
        while True:
            game = new_round()
            if game:
                score += 1
    except:
        print("Game over! Your final score is:", score)

if __name__ == "__main__":
    new_game()
