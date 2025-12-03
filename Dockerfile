# FROM python:3.11-slim

# WORKDIR /app

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# EXPOSE 5000

# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
# # Use Gunicorn as the WSGI server to run the Flask application

# ============================================

# FROM python:3.11-slim

# WORKDIR /app

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# EXPOSE 5000

# # BUILD_VERSION is passed from Jenkins at runtime
# ENV BUILD_VERSION=local-dev

# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]


# ============================================

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
