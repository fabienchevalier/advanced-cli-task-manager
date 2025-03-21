import unittest
from unittest.mock import patch
from task_manager.core import add_task, delete_task


class TestTaskManager(unittest.TestCase):

    @patch("task_manager.core.save_tasks")
    @patch("task_manager.core.load_tasks", return_value=[])
    def test_add_task(self, mock_load_tasks, mock_save_tasks):
        result = add_task("Test Task", priority=2)
        self.assertEqual(result, "Task 'Test Task' added successfully with priority 2.")

    @patch("task_manager.core.save_tasks")
    @patch(
        "task_manager.core.load_tasks",
        return_value=[{"id": 1, "description": "Test Task", "priority": 2}],
    )
    def test_delete_task(self, mock_load_tasks, mock_save_tasks):
        result = delete_task(1)
        self.assertEqual(result, "Task with ID 1 deleted successfully.")


if __name__ == "__main__":
    unittest.main()
