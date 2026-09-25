# Data Engineering Project

## Overview

This project demonstrates fundamental data engineering practices using Python, Bash, Git, and GitHub.

The project focuses on collecting data from a REST API, storing the data in a landing zone, analyzing application logs using Bash commands, and managing the project using Git branching and pull requests.

## Project Objectives

- Collect data from a REST API
- Store API data as JSON
- Organize data into landing, raw, processed, and archive directories
- Analyze application logs using Bash commands
- Use Python for data ingestion
- Use Git for version control
- Implement Git branching and feature development
- Push project code to GitHub
- Create Pull Requests for feature changes

## Technologies Used

- Python
- Bash / Git Bash
- REST API
- JSON
- Git
- GitHub
- VS Code

## Project Structure

```text
data-engineering-project/
│
├── data/
│   ├── landing/
│   │   ├── customers.csv
│   │   └── users.json
│   ├── raw/
│   ├── processed/
│   └── archive/
│
├── logs/
│   └── application.log
│
├── scripts/
│   ├── api_ingestion.py
│   └── log_analysis.sh
│
├── api/
│
└── docker/
    ├── app.py
    └── Dockerfile
```

## 1. REST API Ingestion

The Python script `scripts/api_ingestion.py` collects user data from the JSONPlaceholder REST API.

### API Flow

```text
REST API
   ↓
Python Requests
   ↓
JSON Response
   ↓
data/landing/users.json
```

### Run the API ingestion

```bash
python scripts/api_ingestion.py
```

Expected output:

```text
Starting API ingestion...
Downloaded 10 records
Saved to data\landing\users.json
```

## 2. Log Analysis

The project contains an application log file:

```text
logs/application.log
```

The Bash script:

```text
scripts/log_analysis.sh
```

analyzes the log file using:

- `wc`
- `grep`
- `awk`
- `sort`
- `uniq`

### Run log analysis

```bash
bash scripts/log_analysis.sh
```

Example output:

```text
==============================
     LOG ANALYSIS REPORT
==============================

Total Records:
10

INFO Records:
8

ERROR Records:
2

ERROR Details:
2026-09-25 09:03:20 ERROR Database connection failed
2026-09-25 09:05:25 ERROR API request failed

Log Level Summary:
      2 ERROR
      8 INFO
```

## 3. Git Workflow

The project uses a feature-based Git workflow.

```text
main
  ↓
develop
  ↓
feature/api-ingestion
```

### Branches

- `main` - main project branch
- `develop` - development branch
- `feature/api-ingestion` - feature development branch

### Example Git commands

```bash
git checkout -b develop
git checkout -b feature/api-ingestion
git add .
git commit -m "Improve API ingestion logging"
git push -u origin feature/api-ingestion
```

A Pull Request is created from:

```text
feature/api-ingestion → develop
```

## 4. Data Flow

```text
External REST API
       │
       ▼
Python API Ingestion
       │
       ▼
JSON Data
       │
       ▼
data/landing/users.json


Application Logs
       │
       ▼
Bash Log Analysis
       │
       ├── Total Records
       ├── INFO Records
       ├── ERROR Records
       └── Error Details
```

## 5. Key Skills Demonstrated

- Python programming
- REST API integration
- JSON processing
- File handling
- Bash scripting
- Linux/Unix-style command-line operations
- Log analysis
- Data ingestion
- Git version control
- Git branching
- GitHub repository management
- Pull Request workflow

## 6. Future Improvements

Possible future enhancements include:

- Add automated data validation
- Add data transformation and cleaning
- Add database storage
- Add automated testing
- Add CI/CD using GitHub Actions
- Add Docker containerization
- Add cloud storage integration
- Add an ETL/ELT pipeline
