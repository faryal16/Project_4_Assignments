# Write a program which asks the user how tall they are and 
# prints whether or not they're taller than a pre-specified minimum height.

MIN_HEIGHT = 50

def tall_enough_extension():
    while True:
        height_input = input("\n\033[1;3mHow tall are you? (Press Enter to quit) \033[0m ")
        
        if height_input == "":
            print("\nGoodbye!")
            break
        
        try:
            height = int(height_input)
            
            if height >= MIN_HEIGHT:
                print("\nYou're tall enough to ride!\n")
                break
            else:
                print("You're not tall enough to ride, but maybe next year!\n")
        
        except ValueError:
            print("Please enter a valid number!\n")


if __name__ == "__main__":
    tall_enough_extension()
