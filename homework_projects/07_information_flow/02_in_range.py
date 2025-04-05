# Implement the following function which takes in 3 integers as parameters:

def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive.
    high is guaranteed to be greater than low.
    """
    return low <= n <= high  # Check if n is within the inclusive range [low, high]

def main():
    try:
        # Taking user input
        n = int(input("\033[1;34mEnter the number to check: \033[0m"))
        low = int(input("\033[1;34mEnter the low range value: \033[0m"))
        high = int(input("\033[1;34mEnter the high range value: \033[0m"))
        
        # Call in_range function and display result
        if in_range(n, low, high):
            print(f"\n{n} is between {low} and {high}, inclusive!")
        else:
            print(f"\n{n} is NOT between {low} and {high}, inclusive.")
    
    except ValueError as e:
        print(f"\nError: {e}")
        
if __name__ == "__main__":
    main()
