def add_task(todo_list, task):
    if task.strip() == "":
        print("Task cannot be empty.")
        return
    todo_list.append(task)
    print(f"Added task: {task}")

def remove_task(todo_list, index):
    if 0 <= index < len(todo_list):
        removed = todo_list.pop(index)
        print(f"Removed task: {removed}")
    else:
        print("Invalid task number.")

def show_tasks(todo_list):
    if not todo_list:
        print("No tasks in the list.")
    else:
        print("Your tasks:")
        for i, task in enumerate(todo_list):
            print(f"{i}. {task}")

def main():
    todo_list = []
    while True:
        print("\n--- Todo List Menu ---")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_tasks(todo_list)
        elif choice == "2":
            task = input("Enter the task to add: ")
            add_task(todo_list, task)
        elif choice == "3":
            try:
                index = int(input("Enter the task number to remove: "))
                remove_task(todo_list, index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
