# CI/CD Pipeline Demo (Flask + Jenkins + Docker)

A small **state-of-the-art CI/CD demo project** using:

- Python + Flask
- HTML + CSS UI
- Docker
- Jenkins
- pytest + flake8

The goal is to demonstrate a **real-world CI/CD pipeline** with:

- Automated tests
- Linting
- Dockerized deployment
- Versioned builds
- Health checks
- Build metadata shown in the UI

---

## 🧱 Tech Stack

- **Backend:** Python 3.x, Flask
- **Frontend:** Jinja2 templates, CSS
- **CI/CD:** Jenkins (Declarative Pipeline)
- **Container:** Docker
- **Testing:** pytest
- **Linting:** flake8

---

## 🗂 Project Structure

```text
cicd-pipeline/
├─ app.py
├─ requirements.txt
├─ Dockerfile
├─ Jenkinsfile
├─ README.md
├─ templates/
│   └─ index.html
├─ static/
│   └─ style.css
└─ tests/
    └─ test_app.py


# CI/CD Pipeline — Task Tracker (MySQL)

Simple Flask app with MySQL backend.
Used to demonstrate Jenkins CI/CD + Docker.

## Run locally

1. Ensure MySQL is running and has DB `cicd`.
2. Create table:
   ```sql
   CREATE TABLE tasks (
     id INT AUTO_INCREMENT PRIMARY KEY,
     title VARCHAR(255) NOT NULL,
     status VARCHAR(50) NOT NULL DEFAULT 'pending'
   );
