# Guess My Number
import random

def main():
    
    random_num = random.randint(0,99)
    print("\nI am thinking of a number between 0 and 99...")
    
    guess = int(input("\n\033[1;3;34mEnter a guess: \033[0m"))
    
    while guess != random_num:
        if guess > random_num:
            print("Your guess is too high!!")
        else:
            print("Your guess is too low!!")
        
        guess = int(input("\n\033[1;3;34mEnter a guess: \033[0m"))
        
    print(f"Congrats! The number was: {random_num}")
        
if __name__ == '__main__':
    main()