# Finzome Submission

This repository contains my submission for the Finzome Task 1 and Task 2.

## Task 1: Nifty50 Volatility Calculator

### Description
The Task 1 implementation is a Python backend project that calculates the Daily and Annualized Volatility of Nifty50 data. The dataset includes information such as Date, Open, High, Low, Close, Shares Traded, and Turnover.

### Implementation Details
- **File**: `nifty50_volatility_calculator.py`
- **Dependencies**: See `requirements.txt`

#### Task 1 Formulas Implemented:
1. Daily Returns: (current close / previous close) - 1
2. Daily Volatility: Standard Deviation (Daily Returns)
3. Annualized Volatility: Daily Volatility * Square Root (length of data)

### Usage
1. Install dependencies using `pip install -r requirements.txt`
2. Run the script: `python nifty50_volatility_calculator.py`

## Task 2: Django Volatility Calculator API

### Description
Task 2 is implemented as a Django web application providing a REST API for calculating Daily and Annualized Volatility. The API accepts a CSV file or a parameter to fetch data, computes the volatility, and returns the results.

### Implementation Details
- **Framework**: Django
- **Endpoint**: `/`
- **File**: `volatility_app/views.py`
- **Dependencies**: See `requirements.txt`

### Usage
1. Install dependencies using `pip install -r requirements.txt`
2. Run the Django development server: `python manage.py runserver`
3. Access the API endpoint: `http://127.0.0.1:8000`

#### API Parameters:
- **CSV File**: Upload a CSV file via POST request.
- **File Path**: Specify the file path in the request parameters.

### Note
Ensure you have the necessary data files for both tasks before running the scripts or API.

Feel free to reach out if you have any questions or need further assistance.
