from sklearn.preprocessing import OneHotEncoder, StandardScaler
from scipy import stats
import numpy as np
import pandas as pd

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path, encoding="ISO-8859-1")

    
    drop_cols = ["Unnamed: 0", "id", "member_id", "zip_code", "next_pymnt_d"]
    df.drop(columns=drop_cols, inplace=True)

    for col in df.columns:
        if df[col].dtype == "object":
            df[col].fillna(df[col].mode()[0], inplace=True)  # Replace categorical NaNs with mode
        else:
            df[col].fillna(df[col].median(), inplace=True)  # Replace numerical NaNs with median

    categorical_cols = df.select_dtypes(include=["object"]).columns
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    numerical_cols = df.select_dtypes(include=[np.number]).columns

    scaler = StandardScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    return df

if __name__ == "__main__":
    df = load_and_clean_data("./data/dataset.csv")
    print(df.head())



