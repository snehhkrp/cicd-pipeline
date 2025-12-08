"""Database helper for Task Tracker.

Provides simple functions that the app imports directly.
This module connects to MySQL using environment variables.

For local runs:
  host = "localhost"

For Docker runs:
  set DOCKER_ENV=true to use host.docker.internal
"""

import os
import mysql.connector
from mysql.connector import Error


def _db_config():
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


def get_all_tasks():
    """Return list of tasks as dictionaries.

    If DB is unavailable, return empty list to keep UI usable.
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


def add_task(title):
    """Insert a new task with status 'pending'."""
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO tasks (title, status) VALUES (%s, %s)",
        (title, "pending"),
    )
    conn.commit()
    cur.close()
    conn.close()


def get_tasks():
    """Alias used by app.py and tests."""
    return get_all_tasks()