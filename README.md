# Weather Data Pipeline

A data engineering project that collects current weather data from the Open-Meteo API, processes it using Apache Airflow, stores it in PostgreSQL, and performs basic data analysis and visualization.

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
      ↓
Analysis & Visualization

The pipeline retrieves current weather information for Tehran, passes the extracted data between Airflow tasks using XCom, and stores the result in a PostgreSQL database.

The project also includes a separate analysis step using Pandas and Matplotlib to inspect the stored weather data and visualize temperature changes over time.

## Technologies

- Python
- Apache Airflow
- Docker
- Docker Compose
- PostgreSQL
- Redis
- CeleryExecutor
- Requests
- Psycopg2
- Pandas
- Matplotlib
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
│   ├── analysis.py
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

Generated files and local runtime data such as logs/, __pycache__/, and .pyc files are excluded from version control through .gitignore.

## Pipeline Workflow

### Extract

The `extract_weather` task sends a request to the Open-Meteo API and retrieves the current weather data.

The extracted data includes:

- Latitude
- Longitude
- Current temperature
- Current time

The API request is handled using the Python Requests library.

The extracted data is passed to the next Airflow task using XCom.

### Load

The `load_weather` task receives the extracted data from the `extract_weather` task through Airflow XCom.

The data is then inserted into PostgreSQL.

If the target table does not already exist, it is created automatically.

The database table uses a unique constraint on:

- latitude
- longitude
- time

This prevents the same weather observation from being inserted multiple times.

Duplicate records are ignored using PostgreSQL `ON CONFLICT`.

## Airflow DAG

The DAG is named:

`weather_pipeline`

The task dependency is:

`extract_weather >> load_weather`

The DAG is scheduled to run automatically every day at 00:00 and 12:00 using the Asia/Tehran timezone.
Catchup is disabled to prevent previously missed scheduled runs from being executed.

The project uses:

`CeleryExecutor`

Redis is used as the message broker and PostgreSQL is used as the database.

## Database

The pipeline stores the weather data in a PostgreSQL table named:

`weather_data`

The table contains:

| Column | Type |
|---|---|
| id | SERIAL |
| latitude | FLOAT |
| longitude | FLOAT |
| temperature | FLOAT |
| time | TIMESTAMP |

The combination of latitude, longitude, and time is unique to prevent duplicate weather observations.

Example query:

SELECT *
FROM weather_data
ORDER BY id DESC;

## Data Analysis

The project includes an `analysis.py` script for analyzing the stored weather data.

The analysis uses Pandas to:

- Load weather data from PostgreSQL.
- Display the DataFrame.
- Check data types.
- Check missing values.
- Check duplicate rows.
- Calculate the average temperature.
- Count the number of records.
- Find the maximum temperature.
- Identify the first and last records.
- Calculate the time range.
- Generate descriptive statistics.

The project also uses Matplotlib to visualize temperature changes over time.

## Visualization

The temperature data can be visualized using a line chart.

The chart shows:

- Time on the X-axis.
- Temperature in Celsius on the Y-axis.
- Individual observations using markers.

The chart is titled:

`Temperature Over Time`

This provides a simple visual representation of the collected weather observations and their temperature changes over time.

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

The Airflow environment uses `CeleryExecutor`.
Redis is used for communication between Airflow components and workers.
PostgreSQL stores Airflow metadata and the weather data.

## Configuration
Environment-specific configuration is stored in:
`.env`

The `.env` file is excluded from version control because it contains local configuration and sensitive values.
The Airflow user ID is configured through:
`AIRFLOW_UID=50000`

## Dockerfile
The project uses a custom Airflow image based on:
`apache/airflow:3.0.4`
The required Python packages are installed during the Docker image build.

## Running the Project
Navigate to the project directory:
cd "C:\Users\TabiBitaEng\Desktop\py project 1\airflow"

Start the Docker environment:
docker compose up -d

Check the status of the services:
docker compose ps

Open the Airflow web interface:
http://localhost:8080

The `weather_pipeline` DAG runs automatically according to its schedule.

## Verifying the Pipeline
After a successful DAG execution:

1. The `extract_weather` task should succeed.
2. The extracted data should be passed to the next task through XCom.
3. The `load_weather` task should succeed.
4. The weather data should be stored in PostgreSQL.

The result can be verified using:

SELECT *
FROM weather_data
ORDER BY id DESC;

## Data Validation

The project performs basic validation during analysis.

The following checks are performed:

- Missing values
- Duplicate rows
- Number of records
- Temperature statistics
- First and last observation times
- Time range of the collected data

The database also prevents duplicate observations based on latitude, longitude, and time.

## Git Version Control

The project is prepared to be added to Git.

The `.gitignore` file excludes generated and environment-specific files such as:

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

Before pushing the project, verify that `.env`, `logs`, and generated Python cache files are excluded:

git status

## Git Security

The `.env` file must not be committed to the repository.

Local configuration and sensitive values should remain outside version control.

The repository should contain the project source code, Airflow configuration, Docker configuration, analysis code, and documentation, but not local secrets or generated logs.

## Project Status

The project currently provides a working end-to-end weather data pipeline.

The pipeline successfully:

- Retrieves current weather data from the Open-Meteo API.
- Executes the workflow through Apache Airflow.
- Passes data between tasks using XCom.
- Stores weather data in PostgreSQL.
- Prevents duplicate weather observations using a database unique constraint.
- Runs the Airflow environment through Docker Compose.
- Uses CeleryExecutor.
- Uses Redis as the message broker.
- Uses an Airflow Worker for task execution.
- Performs basic data validation and analysis using Pandas.
- Generates a temperature-over-time visualization using Matplotlib.
- Provides a structured project layout.
- Is ready to be placed under Git version control.

## Future Improvements

Possible future improvements include:

- Adding additional weather parameters.
- Supporting multiple cities.
- Adding scheduled DAG execution.
- Adding more advanced data validation.
- Adding automated tests.
- Improving monitoring and alerting.
- Expanding the PostgreSQL schema.
- Adding more advanced transformation steps.
- Improving data visualization.
- Adding additional analytical metrics.
- Creating a more complete data quality layer.
- Improving pipeline scalability and reliability.