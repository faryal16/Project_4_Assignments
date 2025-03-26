# Simulate rolling two dice, three times. Prints the results 
# of each die roll. This program is used to show how variable scope works.

import random

# NUmber sides of die to roll
NUM_SIDES = 6

def roll_dice():
    """Simulate rolling two dice and print their total"""
    die1 : int =random.randint(1, NUM_SIDES)
    die2 : int =random.randint(1, NUM_SIDES)
    
    total :int = die1 + die2
    
    return total
    
    
def main():
    die1:int = 10
    print("diel in main() start as: " + str(die1))
    
    print("Total of two dice:", roll_dice())
    print("Total of two dice:", roll_dice())
    print("Total of two dice:", roll_dice())
    
    print("diel in main() is: " + str(die1))
    

if __name__ == '__main__':
    main()