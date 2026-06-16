# 📝 DecodeLabs To-Do List App

> A terminal-based student task management application built with Python — Task 1

---

## 📌 Overview

The **DecodeLabs To-Do List App** is a command-line application designed to help manage and track student tasks. It allows users to add tasks with student details, view all tasks with their current status, mark tasks as completed, and delete tasks — all through a simple interactive menu.

---

## 🚀 Features

- ✅ **Add Tasks** — Register student name, roll number, task name, and due date
- 📋 **View Tasks** — Display all tasks with their completion status
- ✔️ **Mark as Completed** — Update the status of any task to "Completed"
- 🗑️ **Delete Tasks** — Remove tasks by their index number
- 🔁 **Interactive Menu Loop** — Continuous prompts until the user chooses to exit

---

## 🛠️ Tech Stack

| Technology | Details         |
|------------|-----------------|
| Language   | Python 3.x      |
| Paradigm   | Object-Oriented |
| Interface  | Command-Line    |
| Libraries  | None (built-in) |

---

## 📂 Project Structure

```
DecodeLabs-ToDo-App/
│
├── todo_app.py       # Main application file
└── README.md         # Project documentation
```

---

## ⚙️ How to Run

### Prerequisites

- Python 3.x installed on your system

### Steps

```bash
# 1. Clone or download the project
git clone https://github.com/your-username/decodelabs-todo-app.git

# 2. Navigate into the project folder
cd decodelabs-todo-app

# 3. Run the application
python todo_app.py
```

---

## 🖥️ Usage

Once the program runs, you'll see the following menu:

```
===================================
               MENU
===================================
1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Exit
```

### Example Workflow

**Adding a Task:**
```
Enter choice: 1
Enter Student Name: Ali Hassan
Enter Roll Number: 221
Enter Task Name: Submit Lab Report
Enter Date (DD-MM-YYYY): 20-06-2025
Task Added Successfully!
```

**Viewing Tasks:**
```
-----------------------------------
Task Number: 0
Student Name: Ali Hassan
Student Roll Number: 221
Task: Submit Lab Report
Task Date: 20-06-2025
Status: Not Completed
```

**Marking as Completed:**
```
Enter choice: 3
Enter Task Number: 0
Task Completed!
```

**Deleting a Task:**
```
Enter choice: 4
Enter Task Number: 0
Task Deleted Successfully!
```

---

## 🧱 Class Design

### `Task`
Represents an individual student task.

| Attribute       | Type    | Description                          |
|----------------|---------|--------------------------------------|
| `Studentname`  | `str`   | Name of the student                  |
| `Rollnum`      | `str`   | Student's roll number                |
| `Taskname`     | `str`   | Name/description of the task         |
| `date`         | `str`   | Due date in DD-MM-YYYY format        |
| `completed`    | `bool`  | Task completion status (default: False) |

| Method                  | Description                        |
|-------------------------|------------------------------------|
| `Show_completed_task()` | Marks the task as completed        |

---

### `ToDoListApp`
Manages the collection of tasks.

| Method                                          | Description                              |
|-------------------------------------------------|------------------------------------------|
| `add_details(name, rollno, taskname, date)`     | Creates and adds a new Task object       |
| `view_details()`                                | Prints all tasks with their status       |
| `completed_task(index)`                         | Marks the task at the given index as done |
| `deleted_task(index)`                           | Removes the task at the given index      |

---

## 🔮 Future Improvements

- [ ] Save tasks to a file (JSON/CSV) for persistence across sessions
- [ ] Add input validation for date format and roll number
- [ ] Implement task search and filter functionality
- [ ] Add a priority level field (High / Medium / Low)
- [ ] Build a GUI version using `tkinter` or a web version with Flask

---

## 👨‍💻 Author

**DecodeLabs — Project 1**

> Built as part of the DecodeLabs Python learning series.

---

## 📄 License

This project is open-source and free to use for educational purposes.
