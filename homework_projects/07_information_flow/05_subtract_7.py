# Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function! 

def subtract_seven(num):
    num = num - 7
    return num

def main():
    user_num: int = int(input("\nEnter a num: "))
    num = subtract_seven(user_num)
    print(f"this should be {num} after substracting from {user_num}")

if __name__ == '__main__':
    main()

    