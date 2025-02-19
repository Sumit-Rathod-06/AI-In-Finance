import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)
    
    df.fillna(df.median(), inplace=True)

    scaler = MinMaxScaler()
    numeric_cols = ['income', 'spending_habit', 'transaction_frequency', 'social_media_score', 'loan_amount', 'credit_utilization']
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    return df

if __name__ == "__main__":
    df = load_and_clean_data("./data/dataset.csv")
    print(df.head())
