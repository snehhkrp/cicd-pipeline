import os
import sys

# Add project root to module path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from db import add_task, get_tasks  # noqa: E402


def test_add_task_and_get_tasks():
    add_task("Sample Task")
    tasks = get_tasks()

    assert isinstance(tasks, list)
    assert any("Sample Task" in t["title"] for t in tasks)
 