from datetime import datetime

def validate_task_title(title):
    if len(title) < 3:
        raise ValueError("Title must be at least 3 characters long.")
    return True

def validate_task_description(description):
    if len(description) < 5:
        raise ValueError("Description must be at least 5 characters long.")
    if len(description) > 500:
        raise ValueError("Description must be less than 500 characters long.")
    return True

def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Due date must be in YYYY-MM-DD format.")
    return True