# make a function
def main():
    # prompt for temp in Fahrenheit
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    # convert to Celsius
    celsius = (fahrenheit - 32 ) * 5.0 / 9.0
    
    # Print the result with only the Celsius value in bold and italic
    print(f"Temperature: {fahrenheit}F = \033[1;3m{celsius}C\033[0m")

# Call the function
if __name__ == '__main__':
    main()