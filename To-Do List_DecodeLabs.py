#======================================================================
#                   DecodeLabs To-Do List App Project 1
#======================================================================

class Task:

    def __init__(self, Studentname, Rollnum, Taskname, date):
        self.Studentname = Studentname
        self.Rollnum = Rollnum
        self.Taskname = Taskname
        self.date = date
        self.completed = False

    def Show_completed_task(self):
        self.completed = True


class ToDoListApp:

    def __init__(self):
        self.tasks = []  # Empty List

    #                                         ---:( Adding Task's ):---

    def add_details(self, Studentname, Rollnum, Taskname, date):
        add_task = Task(Studentname, Rollnum, Taskname, date)
        self.tasks.append(add_task)
        print("Task Added Successfully!")

    #                                         ---:( Viewing Task's ):---

    def view_details(self):
        if len(self.tasks) == 0:
            print("No Task's Found!")
            return

        for index, view_tasks in enumerate(self.tasks):
            status = "Completed" if view_tasks.completed else "Not Completed"

            print("-----------------------------------")
            print("Task Number:", index)
            print("Student Name:", view_tasks.Studentname)
            print("Student Roll Number:", view_tasks.Rollnum)
            print("Task:", view_tasks.Taskname)
            print("Task Date:", view_tasks.date)
            print("Status:", status)

    #                                    ---:( Checking Task's Status ):---

    def completed_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].Show_completed_task()
            print("Task Completed!")
        else:
            print("Invalid Task Number!")

    #                                      ---:( Deleting Task's ):---

    def deleted_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            print("Task Deleted Successfully!")
        else:
            print("Invalid Task!")



    #                                        ---:( Main Program ):---

todo = ToDoListApp()

while True:
    print("===================================")
    print("               MENU                ")
    print("===================================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter choice:\n")

    if choice == "1":
        name = input("Enter Student Name:\n")
        rollno = input("Enter Roll Number:\n")
        taskname = input("Enter Task Name:\n")
        date = input("Enter Date (DD-MM-YYYY):\n")
        todo.add_details(name, rollno, taskname, date)

    elif choice == "2":
        todo.view_details()

    elif choice == "3":
        num = int(input("Enter Task Number:\n"))
        todo.completed_task(num)

    elif choice == "4":
        num = int(input("Enter Task Number:\n"))
        todo.deleted_task(num)

    elif choice == "5":
        print("Exiting..........")
        break

    else:
        print("Invalid choice")