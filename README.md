# Research Submission & Review System

A Flask-based web application for managing research submissions, reviewer assignments, and evaluation workflows.

---

# Features

- Research paper submission
- Reviewer assignment system
- Evaluation and scoring
- SQLite database integration
- Flask web interface
- Virtual environment support
- Automated setup using Makefile

---

# Project Structure

```text
project/
│
├── app.py
├── requirements.txt
├── Makefile
├── research.db
│
├── Controllers/
├── BusinessLogic/
├── Templates/
├── Static/
└── README.md
```

---

# Requirements

- Python 3.10+
- pip
- virtualenv (recommended)

---

# Clone Repository

```powershell
git clone <repository-url>
cd project
```

---

# Create Virtual Environment

## Windows PowerShell

```powershell
python -m venv venv
```

---

# Activate Virtual Environment

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks execution:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate again:

```powershell
.\venv\Scripts\activate
```

---

# Install Dependencies

Using pip:

```powershell
pip install -r requirements.txt
```

---

# Run the Flask Application

```powershell
python app.py
```

Application runs on:

```text
http://127.0.0.1:5000
```

---

# requirements.txt

```text
Flask==3.1.0
Werkzeug==3.1.3
Jinja2==3.1.6
itsdangerous==2.2.0
click==8.1.8
blinker==1.9.0
```

---

# Makefile

```make
install:
	pip install -r requirements.txt

run:
	python app.py

freeze:
	pip freeze > requirements.txt
```

---

# Using Makefile

## Install dependencies

```powershell
make install
```

## Run application

```powershell
make run
```

## Update requirements.txt

```powershell
make freeze
```

---

# Database

The application uses SQLite.

Database file:

```text
research.db
```

Tables are automatically created on application startup.

---

# Deactivate Virtual Environment

```powershell
deactivate
```

---

# Future Improvements

- Authentication system
- Reviewer dashboard
- REST API support
- Email notifications
- Docker support

---

# License

None
