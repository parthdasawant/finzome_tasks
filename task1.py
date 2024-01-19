import pandas as pd
import numpy as np

def calculate_volatilities(data_file):
    """
    Calculates daily and annualized volatility for the given dataset.

    Args:
        data_file (str): Path to the CSV file containing the dataset.

    Returns:
        tuple: (daily_volatility, annualized_volatility)
    """

    # Load the data from the CSV file
    data = pd.read_csv(data_file)

    # Calculate daily returns, handling potential NaN values
    daily_returns = data['Close '].pct_change().dropna()

    # Calculate daily volatility
    daily_volatility = daily_returns.std()

    # Calculate annualized volatility using the common assumption of 252 trading days
    annualized_volatility = daily_volatility * np.sqrt(248)

    return daily_volatility, annualized_volatility

# Example usage:
if __name__ == "__main__":
    data_file = "temp.csv"  # Replace with the actual file path
    daily_volatility, annualized_volatility = calculate_volatilities(data_file)
    print("Daily Volatility:", daily_volatility)
    print("Annualized Volatility:", annualized_volatility)