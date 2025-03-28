# Ask the user for two numbers, one at a time, and then print the result of dividing
# the first number by the second and also the remainder of the division.

def main():
    divided :int =int(input("\n\033[1;3mPlease enter an integer to be divided: \033[0m"))
    divide_by :int =int(input("\n\033[1;3mPlease enter an integer to be divide by: \033[0m"))

    # check for division by zero
    if divide_by == 0:
        print("\n\033[1;31mError: Division by zero is not allowed.\033[0m")
        return  # Exit the function
    
    quotient: int = divided // divide_by # divide with no reminder
    reminder: int = divided % divide_by
    
    print(f"\nThe result of this division is \033[1;3m{quotient}\033[0m with a remainder of \033[1;3m{reminder}\033[0m")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()