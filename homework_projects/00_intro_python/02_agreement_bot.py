# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" 
# (the blank should be filled in with the user-inputted animal, of course).

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