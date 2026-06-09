from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

tasks = []

def add_task(title, description, due_date):
    validate_task_title(title)
    validate_task_description(description)
    validate_due_date(due_date)
    tasks.append({"title": title, "description": description, "due_date": due_date, "completed": False})
    print("Task added successfully!")

def mark_task_as_complete(index, tasks=tasks):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task index.")

def view_pending_tasks(tasks=tasks):
    pending = [t for t in tasks if not t["completed"]]
    if not pending:
        print("No pending tasks.")
    for i, task in enumerate(pending):
        print(f"{i + 1}. [{task['due_date']}] {task['title']} - {task['description']}")

def calculate_progress(tasks=tasks):
    if not tasks:
        progress = 0
    else:
        progress = (sum(1 for t in tasks if t["completed"]) / len(tasks)) * 100
    return progress
