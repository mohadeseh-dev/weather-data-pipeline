# Weather Data Pipeline

A data engineering project that collects current weather data from the Open-Meteo API and stores it in PostgreSQL using Apache Airflow.

## Project Overview

This project implements an ETL pipeline with three main stages:

Open-Meteo API
      ↓
Extract
      ↓
Apache Airflow
      ↓
Load
      ↓
PostgreSQL

The pipeline retrieves current weather information for Tehran, passes the extracted data between Airflow tasks using XCom, and stores the result in a PostgreSQL database.

## Technologies

- Python
- Apache Airflow
- Docker
- Docker Compose
- PostgreSQL
- Redis
- Requests
- Psycopg2
- Python-dotenv
- Open-Meteo API
## Project Structure

airflow/
│
├── config/
│   └── airflow.cfg
│
├── dags/
│   └── weather_pipeline.py
│
├── data/
│   ├── raw_data/
│   └── weather.json
│
├── plugins/
│
├── source/
│   ├── api_to_json.py
│   ├── extract.py
│   ├── load.py
│   └── main.py
│
├── .env
├── .gitignore
├── docker-compose.yaml
├── Dockerfile
├── README.md
└── requirement.txt

## Pipeline Workflow

### Extract

The `extract_weather` task sends a request to the Open-Meteo API and retrieves the current weather data.

The extracted data includes:

- Latitude
- Longitude
- Current temperature
- Current time

The API request is handled using the Python Requests library.

### Load

The `load_weather` task receives the extracted data from the `extract_weather` task through Airflow XCom.

The data is then inserted into PostgreSQL.

If the target table does not already exist, it is created automatically.

## Airflow DAG

The DAG is named:

weather_pipeline

The task dependency is:

extract_weather >> load_weather

The DAG uses manual triggering and has catchup disabled.
## Database

The pipeline stores the weather data in a PostgreSQL table named:

weather_data

The table contains:

| Column | Type |
|---|---|
| id | SERIAL |
| latitude | FLOAT |
| longitude | FLOAT |
| temperature | FLOAT |
| time | TIMESTAMP |

Example query:

SELECT *
FROM weather_data
ORDER BY id DESC;

## Docker Environment

The project runs Apache Airflow using Docker Compose.

The environment contains the following services:

- Airflow API Server
- Airflow Scheduler
- Airflow DAG Processor
- Airflow Worker
- Airflow Triggerer
- PostgreSQL
- Redis

## Configuration

Environment-specific configuration is stored in:

.env

The .env file is excluded from version control because it contains local configuration.

The Airflow user ID is configured through:

AIRFLOW_UID=50000

## Running the Project

Navigate to the project directory:

cd "C:\Users\TabiBitaEng\Desktop\py project 1\airflow"

Start the Docker environment:

docker compose up -d

Check the status of the services:

docker compose ps

Open the Airflow web interface:

http://localhost:8080

Trigger the weather_pipeline DAG from the Airflow interface.
## Verifying the Pipeline

After a successful DAG execution:

1. The extract_weather task should succeed.
2. The extracted data should be passed to the next task through XCom.
3. The load_weather task should succeed.
4. The weather data should be stored in PostgreSQL.

The result can be verified using:

SELECT *
FROM weather_data
ORDER BY id DESC;

## Git Version Control

The project is prepared to be added to Git.

The .gitignore file excludes generated and environment-specific files:

.env
__pycache__/
*.pyc
logs/

### Initialize Git

From the project root:

git init

Check the repository status:

git status

Add the project files:

git add .

Create the initial commit:

git commit -m "Initial commit"

### Connect a Remote Repository

Create an empty repository on GitHub or another Git hosting service.

Then connect the local project to the remote repository:

git remote add origin <repository-url>

Rename the default branch to main:

git branch -M main

Push the project to the remote repository:

git push -u origin main

Before pushing the project, verify that .env, logs, and generated Python cache files are excluded:

git status

## Git Security

The .env file must not be committed to the repository.

Local configuration and sensitive values should remain outside version control.

The repository should contain the project source code, Airflow configuration, Docker configuration, and documentation, but not local secrets or generated logs.

## Project Status

The project currently provides a working end-to-end weather data pipeline.

The pipeline successfully:

- Retrieves weather data from the Open-Meteo API.
- Executes the workflow through Apache Airflow.
- Passes data between tasks using XCom.
- Stores weather data in PostgreSQL.
- Runs the Airflow environment through Docker Compose.
- Uses Redis with CeleryExecutor.
- Provides a structured project layout.
- Is ready to be placed under Git version control.

## Future Improvements

Possible future improvements include:

- Adding additional weather parameters.
- Supporting multiple cities.
- Adding scheduled DAG execution.
- Adding data validation.
- Adding automated tests.
- Improving monitoring and alerting.
- Expanding the PostgreSQL schema.
- Adding more advanced transformation steps.