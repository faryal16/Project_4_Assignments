# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

def main():
    
    side1 :float = float(input("\n\033[1;3mWhat is the length of side 1? \033[0m"))
    side2 :float = float(input("\n\033[1;3mWhat is the length of side 2? \033[0m"))
    side3 :float = float(input("\n\033[1;3mWhat is the length of side 3? \033[0m"))
    
    triangle = str(side1 + side2 + side3)
    
    print(f"\nThe perimeter of the triangle is \033[1;3m{triangle}\033[0m")
    
    
if __name__ == "__main__":
    main()    