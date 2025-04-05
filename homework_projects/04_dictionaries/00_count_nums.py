# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

def get_user_numbers():
    """
    Create an empty list.
    Ask the user to input numbers and store them in a list. 
    Once they enter a blank line, break out of the loop and return the list.
    """
    user_numbers = []
    while True:
        user_input = input("\n\033[1;3;34mEnter a number: \033[0m")
        
        # If the user enters a blank line, break out of the loop and stop asking for input
        if user_input == "":
            break
        
        # Check if the user input is a valid number
        if user_input.isdigit():
            num = int(user_input)
            user_numbers.append(num)
        else:
            print("\033[1;31mPlease enter a valid number.\033[0m")  # Red message for invalid input
    
    return user_numbers

def count_nums(num_lst):
    """
    Create an empty dictionary.
    Loop over the list of numbers. 
    If the number is not in the dictionary, add it as a key with a value of 1.
    If the number is in the dictionary, increment its value by 1.
    """
    num_dict = {}
    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    
    return num_dict


def print_counts(num_dict):
    """
    Loop over the dictionary and print out each key and its value.
    """
    for num in num_dict:
        # print(str(num) + " appears " + str(num_dict[num]) + " times.")
        print(f"\n{str(num)}  appears  {str(num_dict[num])}  times.")


def main():
    """
    Ask the user to input numbers and store them in a list. Once they enter a blank line,
    print out the number of times each number appeared in the list.
    """
    user_numbers = get_user_numbers()
    if user_numbers:
        num_dict = count_nums(user_numbers)
        print_counts(num_dict)
    else:
        print("\n No numbers , entered!")


# Python boilerplate.
if __name__ == '__main__':
    main()