import os
import mysql.connector


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", "pass123"),
        database=os.getenv("MYSQL_DB", "cicd")
    )


def save_build_record(b):
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        sql = """
        INSERT INTO builds (build_number, status, duration_sec, timestamp, job_name)
        VALUES (%s, %s, %s, %s, %s)
        """

        cur.execute(sql, (
            b["number"],
            b["result"],
            b["duration_sec"],
            b["timestamp"],
            "cicd-pipeline"
        ))

        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print("DB ERROR:", e)
