
# make a function
def main():
    # ask the user
    user = input("What's your favorite animal? ")
    user = user.upper()
    # print the statement
    print(f"\nMy favorite animal is also \033[1;3m{user}!\033[0m")
    
# call the function
if __name__ == '__main__':
    main()    