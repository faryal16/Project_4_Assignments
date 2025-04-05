# In this program we show an example of using dictionaries to keep track of information in a phonebook.

def read_phone_numbers():
    """
    Ask the user for names/numbers to story in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}
    
    while True:
        name = input("\n\033[1;3;33mName: \033[0m")
        if name == "":
            break
        number = input("\n\033[1;3;33mNumber: \033[0m")
        phonebook[name] = number
    return phonebook


def print_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    for name in phonebook:
        print(f"\n{str(name)} -> {str(phonebook[name])}")
        
def lookup_numbers(phnebook):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    while True:
        name = input("\n\033[1;3;35mEnter name to lookup: \033[0m")
        if name == "":
            break
        if name not in phnebook:
            print(f"\n{name} is not in phonebook.")
        else:
            print(phnebook[name])
            
            
def main():
    phonebook= read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)
    
if __name__ == '__main__':
    main()
        
    