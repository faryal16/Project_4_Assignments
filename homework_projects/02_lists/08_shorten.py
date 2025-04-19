# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and 
# prints each item it removes until lst is MAX_LENGTH items long.
# If lst is already shorter than MAX_LENGTH you should leave it unchanged.
# We've written a main() function for you which gets
# a list and passes it into your function once you run the program. For the autograder to pass
# you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.

MAX_LENGTH : int = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()
        print(f"\n\033[1;3mRemoved: {last_elem} \033[0m")
    print(f"\n\033[1;3mShortened list: {lst} \033[0m")

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("\nPlease enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("\nPlease enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    print("\nThe full list is:", lst)
    shorten(lst)


if __name__ == '__main__':
    main()