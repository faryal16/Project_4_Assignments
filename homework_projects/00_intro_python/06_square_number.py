# Ask the user for a number and print its square (the product of the number times itself).

def main():
    
    num:float = float(input("\n\033[1;3m Type a number to see its square: \033[0m"))
    
    square :str = str(num**2)
    
    print(f"\n\033[1;3m{num}\033[0m squared is \033[1;3m{square}\033[0m")
    
    
if __name__ == "__main__":
    main()