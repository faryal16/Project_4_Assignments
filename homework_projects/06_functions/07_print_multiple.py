# Fill out print_multiple(message, repeats), which takes as parameters a string message to print, 
# and an integer repeats number of times to print message.

def print_multiple(message: str, repeats: int):
    for i in range(repeats):
        print(message)

# There is no need to edit code beyond this point
def main():
    message = input("\n\033[1;3;34mPlease type a message: \033[0m")
    repeats = int(input("\n\033[1;3;34mEnter a number of times to repeat your message: \033[0m"))
    print_multiple(message, repeats)

if __name__ == '__main__':
    main()
