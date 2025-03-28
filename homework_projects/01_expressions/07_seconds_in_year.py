# Use Python to calculate the number of seconds in a year, and tell the user what 
# the result is in a nice print statement that looks like this (of course the value 5 
# should be the calculated number instead):

def main():
    # define constant
    seconds_per_minute: int = 60
    minutes_per_hour: int = 60
    hours_per_day: int = 24
    days_per_week: int = 7
    days_per_month: int = 30
    days_per_year: int = 365  # Use 366 for leap years
    
     # Calculate the total seconds in a year
    seconds_per_hour: int = seconds_per_minute 
    seconds_per_day: int = seconds_per_minute * minutes_per_hour 
    seconds_per_week: int = seconds_per_minute * minutes_per_hour * hours_per_day * days_per_week
    seconds_per_month: int = seconds_per_minute * minutes_per_hour * hours_per_day * days_per_month
    seconds_per_year: int = seconds_per_minute * minutes_per_hour * hours_per_day * days_per_year
    seconds_per_leapyear: int = seconds_per_minute * minutes_per_hour * hours_per_day * days_per_year + seconds_per_day

    # Print result in a formatted way
    print(f"\nThere are \033[1;3m{seconds_per_hour}\033[0m seconds in a day!")
    print(f"\nThere are \033[1;3m{seconds_per_day}\033[0m seconds in a hour!")
    print(f"\nThere are \033[1;3m{seconds_per_week}\033[0m seconds in a week!")
    print(f"\nThere are \033[1;3m{seconds_per_month}\033[0m seconds in a month!")
    print(f"\nThere are \033[1;3m{seconds_per_year}\033[0m seconds in a year!")
    print(f"\nThere are \033[1;3m{seconds_per_leapyear}\033[0m seconds in a Leap year!")

if __name__ == "__main__":
    main()