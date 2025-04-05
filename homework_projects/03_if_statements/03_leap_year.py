# Write a program that reads a year from the user and tells whether a given year is a leap year or not.

def main():
    # Get the year to check from the user
    year = int(input('\nPlease input a year: '))

    if year % 4 == 0:  # Checking whether the provided year is evenly divisibly by 4
        if year % 100 == 0:  # Checking whether the provided year is evenly divisibly by 100
            if year % 400 == 0:  # Checking whether the provided year is evenly divisibly by 400
                print("\nThat's a leap year!")
            else:  # (Not divisible by 400)
                print("\nThat's not a leap year.")
        else:  # (Not divisible by 100)
            print("\nThat's a leap year!")
    else:  # (Not divisible by 4)
        print("\nThat's not a leap year.")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()