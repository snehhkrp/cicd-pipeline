# from flask import Flask, render_template, request, jsonify
# from db import add_task, get_tasks  # db functions


# app = Flask(__name__)


# @app.route("/")
# def home():
#     tasks = get_tasks()
#     return render_template("index.html", tasks=tasks)


# @app.route("/add", methods=["POST"])
# def add():
#     title = request.form.get("title")
#     if not title:
#         return "Missing title", 400

#     add_task(title)
#     return ("", 204)


# @app.route("/health")
# def health():
#     return jsonify({"status": "ok"})


# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, render_template, request, jsonify
from db import add_task, get_tasks

app = Flask(__name__)


@app.route("/")
def home():
    tasks = get_tasks()
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    if not title:
        return "Missing title", 400

    add_task(title)
    return ("", 204)


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    # MUST NOT use debug=True inside Docker
    app.run(host="0.0.0.0", port=5000)
