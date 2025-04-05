# We've written a helper function for you called greet(name) which takes as input a string name and prints a greeting.

def main():
    name = input("\n\033[1;3mWhat's your name? : \033[0m")
    
    print(f"\nGreetings {name}!")
    
    
if __name__ == '__main__':
    main()