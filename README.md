# portfolio-backend
# **Portfolio Backend**

A backend application for managing a portfolio, built with Python, FastAPI, and SQLAlchemy, and configured with Alembic for database migrations.

---

## **Table of Contents**

1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Setup Instructions](#setup-instructions)
4. [Running the Application](#running-the-application)
5. [Database Migrations](#database-migrations)
6. [Environment Variables](#environment-variables)
7. [Project Structure](#project-structure)
8. [Contributing](#contributing)

---

## **Features**

- User management (authentication, tokens)
- Portfolio components:
  - Job histories
  - Projects
  - Skills
- Fully integrated with Alembic for database migrations
- Uses SQLAlchemy for ORM and model management

---

## **Prerequisites**

Ensure the following are installed:

- Python (>= 3.10)
- Virtualenv or equivalent for Python environment management
- PostgreSQL (or another database supported by SQLAlchemy)
- Node.js (optional, if any frontend dependencies are required)

---

## **Setup Instructions**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/portfolio-backend.git
   cd portfolio-backend
   ```
2. create venv
```python -m venv venv```
3. Start env  
```source venv/bin/activate```
4. Install Dependencies
```pip install -r requirements.txt```
5. Set Up Database
```CREATE DATABASE portfolio_db;```

6. Runninng App
```uvicorn app.main:app --reload```


Product Stucture
```portfolio-backend/
├── alembic/                # Alembic migrations folder
├── app/
│   ├── db/                 # Database utilities
│   ├── models/             # SQLAlchemy models and associations
│   ├── routes/             # FastAPI route handlers
│   ├── services/           # Business logic
│   ├── main.py             # Application entry point
├── .env                    # Environment variables
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
```