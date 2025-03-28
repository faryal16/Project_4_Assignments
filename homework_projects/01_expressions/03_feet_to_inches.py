# Converts feet to inches. Feet is an American unit of measurement.
# There are 12 inches per foot. Foot is the singular, and feet is the plural.

def feet_to_inches(feet:float):
    """Convert feet to inches"""
    return feet * 12

def main():
    feet:float = float(input("\n\033[1mEnter length in feet: \033[0m"))
    inches:float = feet_to_inches(feet)
    
    print(f"\n\033[1;3m{feet} feet is equal to {inches} inches.\033[0m")
    
    

if __name__ == "__main__":
    main()