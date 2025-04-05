# Write a program that loops through a dictionary of fruits, prompting the user to see
# how many of each fruit they want to buy,
# and then prints out the total combined cost of all of the fruits.

def main():
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    
    total_cost = 0
    for fruit_name, price in fruits.items():
        while True:
            try:
                amount_bought = int(input(f"\n\033[1;3mHow many {fruit_name}s do you want to buy? \033[0m"))
                if amount_bought < 0:
                    print("\033[1;31mPlease enter a valid positive number.\033[0m")
                else:
                    break
            except ValueError:
                print("\033[1;31mThat's not a valid number. Please enter a valid positive number.\033[0m")
        
        total_cost += (price * amount_bought)
    print(f"\nYour total is: ${str(total_cost)}" )




if __name__ == '__main__':
    main()