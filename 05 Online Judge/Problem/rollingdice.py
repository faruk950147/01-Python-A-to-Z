'''
what is rolling dice?
- rolling dice is a process of rolling dice and getting a random number between 1 and 6

'''
import random

def roll_dice(min_value=1, max_value=6):
    return random.randint(min_value, max_value)

if __name__ == "__main__":
    while True:
        user_input = input("Do you want to roll the dice? (y/n): ")
        if user_input == "y":
            print(roll_dice(1, 6))
        else:
            print("Goodbye!")
            break
