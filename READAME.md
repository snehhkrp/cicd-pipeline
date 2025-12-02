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
