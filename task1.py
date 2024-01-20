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
    data_file = "temp.csv"  # Replace with the actual file path
    daily_volatility, annualized_volatility = calculate_volatilities(data_file)
    print("Daily Volatility:", daily_volatility)
    print("Annualized Volatility:", annualized_volatility)
