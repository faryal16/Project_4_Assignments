# We want you to gain more experience working with control flow and Booleans in Python.

import random

NUM_ROUNDS = 5

def high_low_game():
    print("\nWelcome to the High-Low Game!\n")
    print("-" * 30)
    
    score = 0
    
    for round in range(1 ,NUM_ROUNDS + 1):
        print(f"\nRound {round}")
        player_number = random.randint(1, 100) 
        computer_number = random.randint(1, 100)
        
        print(f"\nYour number is {player_number}")
        guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
        
        if guess not in ['higher' , 'lower']:
            print("Invalid input. Please type 'higher" or "lower")
            continue #skip the round if input is wrong
        
        if (guess == "higher" and player_number > computer_number) or \
            (guess == "lower" and player_number < computer_number):
                print(f"You were right! The computer's number was {computer_number}")
                score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")

        print(f"Your score is now {score}")

    print("\nThanks for playing!")

    # Optional feedback message
    print("\nYour final score is", score)
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score > NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

def main():
    high_low_game()

if __name__ == "__main__":
    main()