# There are times where we want to return different things from a function based on some condition. 

ADULT_AGE = 18

def is_adult(age: int):
    if age >= ADULT_AGE:
        return True
    
    return False

def main():
    age =int(input("\n\033[1;3;34mHow old is this person?: \033[0m"))
    print(is_adult(age))
    
if __name__ == "__main__":
    main()