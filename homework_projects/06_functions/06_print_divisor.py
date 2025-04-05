# Write the helper function print_divisors(num), which takes in a number and prints all of its divisors

def print_divisiors(num: int):
    print(f"\nHere are the divisiors of {num} ")
    for i in range(num):
        curr_divisor = i + 1
        if num % curr_divisor == 0:
            print(curr_divisor)
            
def main():
    num = int(input("\n\033[1;3;34mEnter a number: \033[0m"))
    print_divisiors(num)
    
if __name__ == '__main__':
    main()
    