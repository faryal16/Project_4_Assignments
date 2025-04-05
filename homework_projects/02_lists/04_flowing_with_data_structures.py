# In the information flow lesson, we discussed using a variable storing a number as an example of scope.
# We saw that changes we made to the number inside a function did not stay unless we returned it. 
# This is true for what we call immutable data types which include things like numbers and strings.

def add_three_copies(my_list, data):
    for i in range(3):
        my_list.append(data)
        

def main():
    message= input("\n\033[1;3m Enter a message to copy: \033[0m")
    my_list = []
    print(f"\nList before: {my_list}")
    add_three_copies(my_list, message)
    print(f"\nList after: {my_list}")
    
if __name__ == "__main__":
    main()