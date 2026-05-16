# End-to-End ETL Data Pipeline

This project demonstrates an end-to-end ETL pipeline using Python, Pandas, PostgreSQL, SQLAlchemy, and Docker.

## Project Overview

The pipeline extracts sales data from a CSV file, cleans and transforms the data using Python/Pandas, and loads the processed data into a PostgreSQL database. SQL queries are included to analyze revenue trends, product performance, and city-level sales.

## Tech Stack

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- Docker
- SQL

## Features

- Extracts raw sales data from CSV
- Cleans missing and duplicate records
- Standardizes column names and text formatting
- Creates calculated revenue fields
- Loads transformed data into PostgreSQL
- Includes SQL analytics queries for business insights

## Folder Structure

```txt
end-to-end-etl-pipeline/
│
├── data/
│   └── sales_data.csv
│
├── scripts/
│   └── etl_pipeline.py
│
├── sql/
│   └── analytics_queries.sql
│
├── docker-compose.yml
├── requirements.txt
└── README.md


CSV File
   ↓
Python + Pandas
(clean & transform data)
   ↓
SQLAlchemy
(connect Python to DB)
   ↓
PostgreSQL
(store data)
   ↓
SQL Queries
(analyze data)
   ↓
DBeaver
(view results)
