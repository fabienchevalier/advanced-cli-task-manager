import json
import os
from task_manager.logger import setup_logger

# Initialize the logger
logger = setup_logger()

# Use an environment variable for the tasks file path or default to "tasks.json"
TASKS_FILE = os.getenv("TASKS_FILE_PATH", "tasks.json")


def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists(TASKS_FILE):
        logger.info(
            f"Task file '{TASKS_FILE}' not found. Starting with an empty task list."
        )
        return []
    with open(TASKS_FILE, "r") as f:
        tasks = json.load(f)
        logger.info(f"Loaded {len(tasks)} tasks from '{TASKS_FILE}'.")
        return tasks


def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)
    logger.info(f"Saved {len(tasks)} tasks to '{TASKS_FILE}'.")


def add_task(description, priority=1):
    """Add a new task."""
    tasks = load_tasks()
    task_id = len(tasks) + 1
    new_task = {"id": task_id, "description": description, "priority": priority}
    tasks.append(new_task)
    save_tasks(tasks)
    logger.info(f"Added task: {new_task}")
    return f"Task '{description}' added successfully with priority {priority}."


def list_tasks():
    """List all tasks."""
    tasks = load_tasks()
    if not tasks:
        logger.info("No tasks found.")
        return "No tasks found."

    task_list = "\n".join(
        [
            f"{task['id']}: {task['description']} (Priority: {task['priority']})"
            for task in tasks
        ]
    )
    logger.info("Listed all tasks.")
    return task_list


def delete_task(task_id):
    """Delete a task by ID."""
    tasks = load_tasks()
    task_to_delete = next((task for task in tasks if task["id"] == task_id), None)

    if not task_to_delete:
        logger.warning(f"Task with ID {task_id} not found.")
        return f"Task with ID {task_id} not found."

    tasks.remove(task_to_delete)
    save_tasks(tasks)
    logger.info(f"Deleted task: {task_to_delete}")
    return f"Task with ID {task_id} deleted successfully."
