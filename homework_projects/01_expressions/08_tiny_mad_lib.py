# Write a program which prompts the user for an adjective, then a 
# noun, then a verb, and then prints a fun sentence with those words!

SENTENCE_START: str = "GIAIC is fun. I learned to program and used Python to make my "  # adjective noun verb

def main():
    # user inputs with bold italic
    adjective: str = input("\n\033[1;3mPlease type an adjective and press enter: \033[0m")
    noun: str = input("\n\033[1;3mPlease type a noun and press enter: \033[0m")
    verb: str = input("\n\033[1;3mPlease type a verb and press enter: \033[0m")

    # Print the final Mad Libs sentence with formatted input
    print(f"\n{SENTENCE_START}\033[1;3m{adjective}\033[0m \033[1;3m{noun}\033[0m \033[1;3m{verb}\033[0m!")

# Call the main function
if __name__ == '__main__':
    main()