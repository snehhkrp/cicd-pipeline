# # from flask import Flask, render_template

# # app = Flask(__name__)

# # @app.route("/")
# # def home():
# #     return render_template("index.html")

# # if __name__ == "__main__":
# #     app.run(host="0.0.0.0", port=5000)


# import os
# from flask import Flask, render_template, jsonify

# app = Flask(__name__)

# # Read build version from env (set by Jenkins)
# BUILD_VERSION = os.getenv("BUILD_VERSION", "dev-local")


# @app.route("/")
# def home():
#     return render_template("index.html", build_version=BUILD_VERSION)


# @app.route("/health")
# def health():
#     """
#     Simple health check endpoint for CI/CD and monitoring.
#     """
#     return jsonify(
#         status="ok",
#         build_version=BUILD_VERSION
#     ), 200


# if __name__ == "__main__":
#     # Local dev only; in Docker we use gunicorn
#     app.run(host="0.0.0.0", port=5000)



#--- app.py revised version ---
from flask import Flask, render_template, jsonify, request
import mysql.connector
import os

app = Flask(__name__)


# ---------------------------------------------------------
# Database Connection (auto-detect: local or container)
# ---------------------------------------------------------
def get_db_connection():
    db_host = "localhost"

    # When running inside Docker
    if os.environ.get("DOCKER_ENV") == "true":
        db_host = "host.docker.internal"

    return mysql.connector.connect(
        host=db_host,
        user="root",
        password="pass123",   # Change if your MySQL password is different
        database="cicd"
    )


# ---------------------------------------------------------
# Routes
# ---------------------------------------------------------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "service": "cicd-demo-app",
        "build_version": os.environ.get("BUILD_VERSION", "local")
    })


# ----------- GET TASKS (READ) ----------------------------
@app.route("/tasks", methods=["GET"])
def get_tasks():
    try:
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()
        cursor.close()
        db.close()

        return jsonify(rows)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ----------- ADD TASK (CREATE) ---------------------------
@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()

    if not data or "title" not in data:
        return {"error": "Title is required"}, 400

    try:
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO tasks (title, status) VALUES (%s, %s)",
            (data["title"], "pending")
        )
        db.commit()
        cursor.close()
        db.close()

        return {"message": "Task added"}, 201

    except Exception as e:
        return {"error": str(e)}, 500


# ---------------------------------------------------------
# Run the app
# ---------------------------------------------------------
if __name__ == "__main__":
    # Running locally
    app.run(host="0.0.0.0", port=5000, debug=True)
