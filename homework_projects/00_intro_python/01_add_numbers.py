def main():
    # Prompt the users
    num1 = input("Enter the first number: ")
    num1 = int(num1)
    
    num2 = input("Enter the second number: ")
    num2 = int(num2)
    
    # Calculate the sum
    result = num1 + num2
    
    # print the results
    # print(f"The sum of {num1} and {num2} is {result}")
    
    
    #  # Print the result in bold and italic using ANSI escape codes
    print(f"The sum of \033[1m{num1}\033[0m and \033[1m{num2}\033[0m is \033[1;3m{result}\033[0m")
#call the function
if __name__ == "__main__":
    main() 