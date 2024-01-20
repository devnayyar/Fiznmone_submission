import os
from django.conf import settings
import pandas as pd
import numpy as np
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

#setting GLOBAL path for the excel sheet which have the data
path = "NIFTY50.xlsx"

def calculate_daily_returns(df):
    """
    Calculate daily returns based on the 'Close' column.

    Parameters:
    - df (pd.DataFrame): Input DataFrame containing the financial data.

    Returns:
    pd.DataFrame: DataFrame with an additional 'Daily Returns' column.
    """
    df['Daily Returns'] = df['Close '].pct_change()
    return df

def calculate_daily_volatility(df):
    """
    Calculate daily volatility based on the 'Daily Returns' column.

    Parameters:
    - df (pd.DataFrame): Input DataFrame containing the financial data.

    Returns:
    float: Daily volatility value.
    """
    daily_volatility = df['Daily Returns'].std()
    return daily_volatility

def calculate_annualized_volatility(daily_volatility, data_length):
    """
    Calculate annualized volatility.

    Parameters:
    - daily_volatility (float): Daily volatility value.
    - data_length (int): Length of the financial data.

    Returns:
    float: Annualized volatility value.
    """
    annualized_volatility = daily_volatility * np.sqrt(data_length)
    return annualized_volatility

@csrf_exempt
@require_http_methods(["GET", "POST"])
def compute_volatility(request):
    """
    Calculate Daily and Annualized Volatility based on financial data.

    Accepts both GET and POST requests.

    Parameters for POST request:
    - 'file_path' (str): Path to the Excel file containing financial data.
    - 'file' (file): File uploaded in the request containing financial data.

    Returns:
    JsonResponse: JSON response containing calculated volatility values.
    """
    try:
        file_name = "NIFTY50.xlsx"  # Adjust the file name as needed
        file_path = os.path.join(settings.BASE_DIR, file_name)

        # Check if the file exists
        if not os.path.isfile(file_path):
            return JsonResponse({"error": f"File not found: {file_path}"}, status=404)

        # Read the Excel file
        df = pd.read_excel(file_path)
        # Calculate Daily Returns
        df = calculate_daily_returns(df)

        # Calculate Daily Volatility
        daily_volatility = calculate_daily_volatility(df)

        # Calculate Annualized Volatility
        data_length = len(df)
        annualized_volatility = calculate_annualized_volatility(daily_volatility, data_length)

        return JsonResponse({
            "Daily Volatility": daily_volatility*100,
            "Annualized Volatility": annualized_volatility*100
        }, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
