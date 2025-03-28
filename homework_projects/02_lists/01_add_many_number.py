# Function to sum a list of numbers
def add_many_numbers(numbers: list[int]) -> int:
    """Takes a list of numbers and returns the sum of those numbers."""
    
    total: int = 0  # Corrected the typo in 'total'
    for number in numbers:
        total += number
        
    return total

def main():
    numbers: list[int] = [1, 2, 3, 4, 5]  # Sample list of numbers
    sum_of_numbers: int = add_many_numbers(numbers)
    
    print(f"\nThe sum of the numbers is: \033[1;3m{sum_of_numbers}\033[0m")  # Bold and italic output

if __name__ == '__main__':
    main()
