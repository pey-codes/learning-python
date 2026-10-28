def add_task():
    task = input("Enter a task: ")

    if task.strip() == "":
        print("You cannot add an empty task.")
    else:
        with open("tasks.txt", "a")as file:
            file.write(task.strip() + "\n")

        print("Task saved!")

def view_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        if len(tasks) == 0:
            print("You have no tasks.")
        
        else:
            print("Your tasks")

            for number, task in enumerate(tasks, start=1):
                print(number, task.strip())

    except FileNotFoundError:
        print("No tasks file found.")

def delete_task():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

            if len(tasks) == 0:
                print("You have no tasks to delete.")
                return
        print("Your tasks:")
        for number, task in enumerate(tasks, start=1):
            print(number, task.strip())
        try:
            task_number = int(input("Enter the number of the task to delete: "))
        except ValueError:
            print("Please enter a number.")
            return

        if task_number >= 1 and task_number <= len(tasks):
            tasks.pop(task_number - 1)

            with open("tasks.txt", "w") as file: 
                file.writelines(tasks)

                print("Task deleted!")

        else: 
            print("That task does not exist.")
    except FileNotFoundError:
        print("No tasks file found.")

def clear_tasks():
    with open("tasks.txt", "w") as file:
        file.write("")

    print("All tasks have been deleted.")

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Clear all tasks")
    print("5. Exit")

    choice = input("Choose an option: ")




    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        clear_tasks()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")                                                                                                                                                                                                                                                                                                            