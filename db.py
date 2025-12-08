"""
Database helper for Task Tracker.

Provides simple functions that the app imports directly.
This module connects to MySQL using environment variables.

For local runs:
  host = "localhost"

For Docker runs:
  set DOCKER_ENV=true to use host.docker.internal
"""

import os
from typing import List, Dict

import mysql.connector
from mysql.connector import Error


def _db_config() -> dict:
    """Return DB connection parameters."""
    if os.getenv("DOCKER_ENV") == "true":
        host = "host.docker.internal"
    else:
        host = os.getenv("MYSQL_HOST", "localhost")

    return {
        "host": host,
        "user": os.getenv("MYSQL_USER", "root"),
        "password": os.getenv("MYSQL_PASSWORD", "pass123"),
        "database": os.getenv("MYSQL_DB", "cicd"),
    }


def _get_conn():
    """Create and return a MySQL connection."""
    cfg = _db_config()
    return mysql.connector.connect(
        host=cfg["host"],
        user=cfg["user"],
        password=cfg["password"],
        database=cfg["database"],
    )


def get_tasks() -> List[Dict]:
    """Return list of tasks as dictionaries.

    If DB is unavailable, return an empty list to keep the UI usable.
    """
    try:
        conn = _get_conn()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT id, title, status FROM tasks ORDER BY id DESC")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except Error:
        return []


# Backwards-compatible alias (some old code called get_all_tasks)
def get_all_tasks() -> List[Dict]:
    """Alias to get_tasks for backward compatibility."""
    return get_tasks()


def add_task(title: str) -> None:
    """Insert a new task with status 'pending'."""
    try:
        conn = _get_conn()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO tasks (title, status) VALUES (%s, %s)",
            (title, "pending"),
        )
        conn.commit()
        cur.close()
        conn.close()
    except Error:
        # swallow DB error to keep UI usable; in prod you would log this
        return
