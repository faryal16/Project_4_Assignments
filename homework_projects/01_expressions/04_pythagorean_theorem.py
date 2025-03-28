# Write a program that asks the user for the lengths of the two perpendicular sides 
# of a right triangle and outputs the length of the third side (the hypotenuse)
# using the Pythagorean theorem!

import math

def main():
    
    ab:float = float(input("\n\033[1;3mEnter the length of AB: \033[0m"))
    ac:float = float(input("\n\033[1;3mEnter the length of AC: \033[0m"))
    
    # Calculate the hypotenuse
    bc:float = math.sqrt(ab**2 +ac**2)
    
    print(f"\nThe length of BC (the hypotenuse) is: \033[1;3m {bc:.2f}\033[0m")
    
if __name__ == "__main__":
    main()