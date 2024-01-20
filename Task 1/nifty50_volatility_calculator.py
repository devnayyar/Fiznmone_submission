import pandas as pd
import numpy as np

# Load the dataset from Excel
def load_dataset(file_path):
    df = pd.read_excel(file_path)
    return df

# Calculate Daily Returns
def calculate_daily_returns(df):
    df['Daily Returns'] = df['Close '].pct_change()
    return df

# Calculate Daily Volatility
def calculate_daily_volatility(df):
    daily_volatility = df['Daily Returns'].std()
    return daily_volatility

# Calculate Annualized Volatility
def calculate_annualized_volatility(daily_volatility, data_length):
    annualized_volatility = daily_volatility * np.sqrt(data_length)
    return annualized_volatility

if __name__ == "__main__":
    # Specify the path to your Excel file
    excel_file_path = 'C:/Users/DEV NAYYAR/Desktop/Finzmone_python/Task 1/NIFTY50.xlsx'

    # Load the dataset from Excel
    nifty_data = load_dataset(excel_file_path)
    # Print the column names to identify the correct column names
    print(nifty_data.columns)


    # Calculate Daily Returns
    nifty_data = calculate_daily_returns(nifty_data)

    # Calculate Daily Volatility
    daily_volatility = calculate_daily_volatility(nifty_data)

    # Calculate Annualized Volatility
    data_length = len(nifty_data)
    annualized_volatility = calculate_annualized_volatility(daily_volatility, data_length)

    # Display the results
    print(f"Daily Volatility: {daily_volatility:.4f}")
    print(f"Annualized Volatility: {annualized_volatility:.4f}")
