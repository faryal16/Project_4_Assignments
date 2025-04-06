# Write a simple joke bot. The bot starts by asking the user what they want. 
# However, your program will only respond to one response: Joke.


# You should use the three constants:

PROMPT = "\n\033[1;34mWhat do you want? \033[0m"  
JOKE = """\nHere is a joke for you! 
Panaversity GPT - Sophia is heading out to the grocery store. 
A programmer tells her: get a liter of milk, and if they have eggs, get 12. 
Sophia returns with 13 liters of milk. 
The programmer asks why and Sophia replies: 'because they had eggs'"""
SORRY = "\nSorry I only tell jokes."

# main programe
def main():
    user_input = input(PROMPT)
    if user_input == "joke":
        print(JOKE)
    else:
        print(SORRY)
        
if __name__ == "__main__":
    main()