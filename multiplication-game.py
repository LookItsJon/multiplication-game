# multipication-game.py

from time import *
import random

def countdown():
    print("Starting in")
    print("3...")
    sleep(1)
    print("2...")
    sleep(1)
    print("1...")
    sleep(1)
    print("GO!")

def generate_new_num():
    return random.randint(1,10)

def print_nums():
    print(first_num, "x", second_num)

score = 0
first_num = generate_new_num()
second_num = generate_new_num()


if __name__ == "__main__":
    #countdown()
    print_nums()