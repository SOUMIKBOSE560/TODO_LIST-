# Function to display the menu options
def display_menu():
    print("To-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Item to To-Do List")
    print("3. Remove Item from To-Do List")
    print("4. Save To-Do List to File")
    print("5. Exit")

# Function to view the current To-Do List
def view_todo_list(todo_list):
    print("To-Do List:")
    for item in todo_list:
        print(item)

# Function to add an item to the To-Do List
def add_item(todo_list):
    item = input("Enter the item to add :")
    todo_list.append(item)
    
#Function to remove item from todo list
def remove_item(todo_list):
    item = input("Enter the item you want to remove :")
    if item in todo_list:
        todo_list.remove(item)
    else:
        print("Item does not exist in the list")
        
#Function to save todo list in a .txt file
def save_to_file(todo_list):
    count = 0
    with open("todo_list.txt","w") as f:
        for item in todo_list:
            count = count + 1
            f.write(count + "> " + item + "\n") 
        
#Main function to run the to do application
def main():
    todo_list = []
    
    while True:
        display_menu()
        
        choice = input("Enter your choice : ")
        
        if(choice == '1'):
            view_todo_list(todo_list)
        elif(choice == '2'):
            add_item(todo_list)
        elif(choice == '3'):
            remove_item(todo_list)
        elif(choice == '4'):
            save_to_file(todo_list)
        elif(choice == '5'):
            print("Exiting..")
            break
        else:
            print("Invalid choice, Please try again..")
            
main()
