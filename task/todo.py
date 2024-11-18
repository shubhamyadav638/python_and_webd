# Initialize an empty to-do list
todo_list = []

# Function to add a task to the to-do list
def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added to the to-do list.")

# Function to remove a task from the to-do list
def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print(f"Task '{task}' removed from the to-do list.")
    else:
        print(f"Task '{task}' not found in the to-do list.")

# Function to display the to-do list
def view_list():
    if not todo_list:
        print("The to-do list is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

# Main program loop
while True:
    print("\nOptions:")
    print("Enter 'add' to add a task")
    print("Enter 'remove' to remove a task")
    print("Enter 'view' to view the to-do list")
    print("Enter 'quit' to exit the program")

    user_input = input("Enter your choice: ").strip().lower()

    if user_input == 'add':
        task = input("Enter the task you want to add: ")
        add_task(task)
    elif user_input == 'remove':
        task = input("Enter the task you want to remove: ")
        remove_task(task)
    elif user_input == 'view':
        view_list()
    elif user_input == 'quit':
        break
    else:
        print("Invalid input. Please try again.")
