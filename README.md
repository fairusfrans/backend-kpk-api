# backend-kpk-api

# KPK Calculator REST API

Backend application for calculating Least Common Multiple (LCM) using Python, FastAPI, and SQLite.

## Technologies
- Python
- FastAPI
- SQLite
- SQL
- REST API

## Features
- Calculate KPK (LCM) of two numbers
- Save calculation history
- View all calculation history
- View history by ID
- Delete calculation history

## Installation

1. Clone repository
2. Install dependencies:

pip install -r requirements.txt

3. Run the application:

uvicorn main:app --reload

## API Documentation

Open:

http://127.0.0.1:8000/docs

## Example Request

POST /kpk

{
  "bilangan1": 12,
  "bilangan2": 18
}

## Expected Result

{
  "hasil_kpk": 36
}
