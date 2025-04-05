# Fill out the get_name() function to return your name as a string!
# We've written a main() function for you which calls your function to retrieve your name and then prints it in a greeting.

def get_name():
    name = input("\n\033[1;3;34mEnter your name: \033[0m")
    return name

def main():
    name = get_name()
    print(f"\nHowdy, {name}! 🤠")
    
if __name__ == '__main__':
    main()