# Write a program that asks a user to enter a number. Your program will then double that number and
# print out the result. It will repeat that process until the value is 100 or greater.

def main():
    user_input = int(input("\n\033[1;34mEnter a number: \033[0m"))
    curr_value = user_input * 2
    
    while curr_value < 100:
        print(curr_value, end=" ")
        curr_value *= 2
        
    print(curr_value)
    
    
    
if __name__ == "__main__":
    main()    
    