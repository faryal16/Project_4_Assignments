# Guess My Number

import random

def main():
    num = random.randint(1, 99)
    
    print("\nI am thinking of a number between 1 and 99...")
    
    while True:
        try:
            guess = input("\n\033[1;34mEnter a guess: \033[0m")
            
            if guess == "":
                print("\nYou have exited the game.")
                break
                
            guess = int(guess)
            
            if guess < num:
                print("Your guess is too low!")
            elif guess > num:
                print("\nYour guess is too high!")
            else:
                print(f"\nCongrats! The number was {str(num)}.")
                break
        except ValueError:
            print("\nInvalid input. Please enter a number.")
    
if __name__ == '__main__':
    main()
