# Expense Tracker CLI Application

A **Command Line Interface (CLI) based Expense Tracker** that ingests CSV files, stores the data in a PostgreSQL database, and runs analytics queries on the stored expense data.

The application follows a **modular Python architecture**, uses **environment variables for configuration**, and supports **automatic CSV ingestion**.

---

# Project Overview

This application performs the following steps:

1. Read expense records from CSV files
2. Validate and process records using Python
3. Store data in a PostgreSQL database
4. Run analytics queries from the CLI

---

# Architecture Diagram

```
                +-------------------+
                |     CSV Files     |
                |  (data folder)    |
                +---------+---------+
                          |
                          v
                +-------------------+
                |   Python CLI App  |
                |                   |
                |  - CSV Ingestion  |
                |  - Data Validation|
                |  - Analytics      |
                +---------+---------+
                          |
                          v
                +-------------------+
                |   PostgreSQL DB   |
                |     (records)     |
                +---------+---------+
                          |
                          v
                +-------------------+
                |   CLI Analytics   |
                |   Output Results  |
                +-------------------+
```

**Data Flow**

```
CSV Files → Python Processing → PostgreSQL → Analytics Output
```

---

# Project Structure

```
expense_tracker
│
├── main.py              # CLI entry point
├── db.py                # PostgreSQL connection + CSV ingestion logic
├── analytics.py         # SQL analytics queries
│
├── data/                # CSV files directory
│   ├── expense_1.csv
│   ├── expense_2.csv
│
├── .env                 # Environment variables
├── requirements.txt     # list of modules & libraries
└── README.md            # documentation of project
```

---

# Prerequisites

Ensure the following tools are installed:

* Python 3.9+
* PostgreSQL
* Docker (optional)
* Git

---

# Virtual Environment Setup

It is recommended to use a **Python Virtual Environment** to isolate project dependencies.

## Create Virtual Environment

Run the following command in the project root folder:

```
python -m venv venv
```

This will create a folder named `venv` that contains a separate Python environment for this project.

---

## Activate Virtual Environment

### On Windows

```
venv\\Scripts\\activate
```

### On Mac / Linux

```
source venv/bin/activate
```

Once activated, your terminal will show:

```
(venv)
```

This means the virtual environment is active.

---

# Install Dependencies

Install all required Python packages using:

```
pip install -r requirements.txt
```

---

# requirements.txt

```
psycopg2-binary
python-dotenv
pydantic
```

---

# Environment Variables

Create a `.env` file in the project root directory.

```
DB_HOST=localhost
DB_NAME=expense
DB_USER=postgres
DB_PASSWORD=your_password
DB_PORT=5433
```

These variables are used by the application to connect to PostgreSQL.

---

# Running the Application

## Ingest CSV Files

Load all CSV files from the `data` directory into the database.

```
python main.py ingest
```

---

## Run Analytics

Execute analytics queries on stored expense data.

```
python main.py
```

Example output:

```
Running Expense Analytics

Total Expense:
12500

Average Expense:
450
```

---

# CSV File Format

CSV files must follow this structure:

```
date,merchant,category,amount
2024-01-01,Amazon,Shopping,1200
2024-01-02,Uber,Transport,300
2024-01-03,Swiggy,Food,450
```

---

# Running with Docker

Start the entire system using Docker:

```
docker compose up
```

This will start:

* PostgreSQL database
* Python application container

---

# Git Workflow

The repository follows a **feature branch workflow**.

Example branches:

```
feature/db-insert
feature/csv-reader
```

Each feature is developed in a separate branch and merged into `main` using a pull request.

---

# Author

Manisha Jangra