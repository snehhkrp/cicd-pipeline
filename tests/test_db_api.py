import sys
import os

# Add project root
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from db import add_task, get_tasks


def test_add_and_get_tasks():
    add_task("Test Task From CI")
    tasks = get_tasks()

    assert isinstance(tasks, list)
    assert any("Test Task From CI" in t["title"] for t in tasks)
