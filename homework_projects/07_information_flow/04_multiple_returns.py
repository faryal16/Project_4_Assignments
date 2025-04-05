# There are times where you are working with lots of different data within a function that you want to return. 

def get_user_info():
    first_name = input("\nWhat is your first name?: ")
    last_name = input("\nWhat is your last name?: ")
    email_address = input("\nWhat is your email address?: ")
    
    return first_name, last_name ,email_address

def main():
    user_data = get_user_info()
    print(f"\nReceived the following user data: \033[1;3;34m{user_data}\033[0m")
    
if __name__ == "__main__":
     main()
