tasks=[]
def show_task():
    if not tasks:
        print("your to-do list is empty.")
    else:
        print("your tasks:")
        for index, task in enumerate(tasks,start=1):
            print(f"{index}.{task}")
def add_task():
    task=input("enter a new task:")
    tasks.append(task)
    print(f"'{task}'has been added to your to-do-list.")
def remove_task():
    show_task()
    try:
        task_number=int(input("enter the task number to remove:"))
        if 1<=task_number<=len(tasks):
            removed_task=tasks.pop(task_number-1 )
            print(f"'{removed_task}'has been removed from your to-do list.")
        else:
            print("invalid task number.")
    except ValueError:
        print("please enter a valid number.")
    while True:
        print("\nChoose an action:")
        print("1. View tasks")
        print("2.Add a task")
        print("3. remove a task")
        print("4. Exit")
        choice=input("enter your choice:")
        if choice=="1":
            show_task()
        elif choice=="2":
            add_task()
        elif choice=="3":
            remove_task()
        elif choice=="4":
            print("goodbye!")
            break
        else:
            print("invalid choice.please choose a valid action.")
