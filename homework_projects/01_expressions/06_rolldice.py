# Simulate rolling two dice, and prints results of each roll as well as the total.

import random

NUM_SIDES: int =6

def main():
    die1:int = random.randint(1, NUM_SIDES)
    die2:int = random.randint(1, NUM_SIDES)
    
    # total calculate
    total : int = die1 + die2
    
    # print results
    print(f"\n🎲 Dice have {NUM_SIDES} sides each.")
    print(f"🎲 First die: \033[1m{die1}\033[0m")
    print(f"🎲 Second die: \033[1m{die2}\033[0m")
    print(f"\n✨ Total of two dice: \033[1;3m{total}\033[0m")

if __name__ == '__main__':
    main()