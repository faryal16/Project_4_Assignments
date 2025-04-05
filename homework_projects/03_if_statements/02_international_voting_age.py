# Write a program which asks a user for their age and lets them know 
# if they can or can't vote in the following three fictional countries.

PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 23
MAYENGUA_AGE : int = 48

def main():
    # Get the user's age
    user_age = int(input("\n\033[1;3;34mHow old are you? \033[0m"))

    # Check if the user can vote in Peturksbouipo
    if user_age >= PETURKSBOUIPO_AGE:
        print(f"\nYou can vote in \033[1;3;34mPeturksbouipo\033[0m where the voting age is \033[1;3;34m{PETURKSBOUIPO_AGE}\033[0m. " )
    else:
        print(f"\nYou cannot vote in \033[1;3;34mPeturksbouipo\033[0m where the voting age is \033[1;3;34m{PETURKSBOUIPO_AGE}\033[0m. ")
    
    # Check if the user can vote in Stanlau
    if user_age >= STANLAU_AGE:
        print(f"You can vote in \033[1;3;34mStanlau\033[0m where the voting age is \033[1;3;34m{STANLAU_AGE}\033[0m." )
    else:
        print(f"You cannot vote in \033[1;3;34mStanlau\033[0m where the voting age is \033[1;3;34m{STANLAU_AGE}\033[0m." )
    
    # Check if user can vote in Mayengua
    if user_age >= MAYENGUA_AGE:
        print(f"You can vote in \033[1;3;34mMayengua\033[0m where the voting age is \033[1;3;34m{MAYENGUA_AGE}\033[0m. " )
    else:
        print(f"You cannot vote in \033[1;3;34mMayengua\033[0m where the voting age is \033[1;3;34m{MAYENGUA_AGE}\033[0m. " )


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()