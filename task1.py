import pandas as pd
import numpy as np


def calculate_volatilities(data_file):
    df = pd.read_csv(data_file)
    df.columns = [col.strip() for col in df.columns]
    daily_returns = df['Close'].pct_change().dropna()
    daily_volatility = daily_returns.std()
    annualized_volatility = daily_volatility * np.sqrt(len(df))
    return daily_volatility, annualized_volatility


if __name__ == "__main__":
    # Replace with the actual file path
    data_file = "NIFTY 50-22-01-2023-to-22-01-2024.csv"
    daily_volatility, annualized_volatility = calculate_volatilities(data_file)
    print("Daily Volatility:", daily_volatility)
    print("Annualized Volatility:", annualized_volatility)
