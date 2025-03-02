def display_menu():
    print("\nMenu:")
    print("1. Add an item to the list")
    print("2. Remove an item from the list")
    print("3. View the list")
    print("4. Search for an item in the list")
    print("5. Exit")

def add_item(my_list):
    item = input("Enter the item to add: ")
    my_list.append(item)
    print(f"'{item}' has been added to the list.")

def remove_item(my_list):
    item = input("Enter the item to remove: ")
    if item in my_list:
        my_list.remove(item)
        print(f"'{item}' has been removed from the list.")
    else:
        print(f"'{item}' not found in the list.")

def view_list(my_list):
    if my_list:
        print("\nList contents:")
        for item in my_list:
            print(f"- {item}")
    else:
        print("The list is empty.")

def search_item(my_list):
    item = input("Enter the item to search: ")
    if item in my_list:
        print(f"'{item}' is in the list.")
    else:
        print(f"'{item}' not found in the list.")

def main():
    my_list = []  # Empty list at the start
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_item(my_list)
        elif choice == '2':
            remove_item(my_list)
        elif choice == '3':
            view_list(my_list)
        elif choice == '4':
            search_item(my_list)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option! Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()
