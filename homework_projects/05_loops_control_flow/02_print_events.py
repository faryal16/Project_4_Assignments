# Write a program that prints the first 20 even numbers. There are several correct approaches,
# but they all use a loop of some sort.Do no write twenty print statements

def main():
    print("\nthe first 20 even numbers.")
    for i in range(40):
        if i % 2 == 0:
            print(i)
            
if __name__ == "__main__":
    main()