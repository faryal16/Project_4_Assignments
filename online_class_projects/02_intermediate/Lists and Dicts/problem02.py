# Problem #2: Index Game

def access_element(lst, index):
    """Return the element at the specified index."""
    if index < 0 or index >= len(lst):
        return "Index out of range"
    
    return lst[index]

def modify_element(lst, index, new_value):
    """Replace the element at the specified index with the new value."""
    if index < 0 or index >= len(lst):
        return "Index out of range"
    
    lst[index] = new_value
    return lst

def slice_list(lst, start , end):
    """Returns a new list containing elements from start to end index."""
    if start < 0 or end > len(lst) or start >= end:
        return "Invalid slice range"
    return lst[start:end]

def game():
    
    my_list = [42, "banana", "apple" , 3.14 , "oranges"]
    
    print("\nWelcome to the Index Game!")
    print("\nHere's the current list:", my_list)
    
    while True:
        # Prompt user to select an operation
        print("\nSelect an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
        
        operation = input("\nEnter the number for the operation you want to perform: ")
        
        if operation == '1':  # Access an element
            index = int(input("Enter the index of the element to access: "))
            result = access_element(my_list, index)
            print("Result:", result)

        elif operation == '2':  # Modify an element
            index = int(input("Enter the index of the element to modify: "))
            new_value = input("Enter the new value: ")
            result = modify_element(my_list, index, new_value)
            print("Updated list:", result)

        elif operation == '3':  # Slice the list
            start = int(input("Enter the start index: "))
            end = int(input("Enter the end index: "))
            result = slice_list(my_list, start, end)
            print("Sliced list:", result)

        elif operation == '4':  # Exit the game
            print("Thanks for playing!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    game()