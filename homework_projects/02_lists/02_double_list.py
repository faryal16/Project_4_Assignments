# Write a program that doubles each element in a list of numbers. 

def main():
    
    numbers:list[int]= [1,2,3,4]
    
    for i in range(len(numbers)):
        num_index = numbers[i]
        numbers[i] =num_index *2
    
    print(f"\nOriginal list: \033[1;3m[1,2,3,4] \033[0m") 
    print(f"\nDoubled list: \033[1;3m{numbers}\033[0m") 
    
if __name__ == '__main__':
    main()