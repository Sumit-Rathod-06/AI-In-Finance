AI-Powered Risk Assessment Using Random Forest
Overview
This project implements a Random Forest classifier to assess borrower risk in micro-finance. The model predicts loan default probability based on both traditional financial metrics (credit score, previous defaults) and non-traditional data (social sentiment, mobile usage, location stability).

Features
✔ Uses traditional & non-traditional financial data for risk assessment
 ✔ Implements Random Forest Classifier for high accuracy
 ✔ Includes data preprocessing and feature selection
 ✔ Outputs borrower risk classification (default vs. no default)

Installation
1. Install Dependencies
pip install -r requirements.txt

2. Dataset
Ensure you have risk_data.csv in your working directory. You can generate a sample dataset using:
import pandas as pd
import numpy as np

# Generate sample data
data = {
    "credit_score": np.random.randint(500, 800, 100),
    "social_sentiment": np.round(np.random.uniform(-1, 1, 100), 2),
    "mobile_usage": np.round(np.random.uniform(2, 8, 100), 1),
    "location_stability": np.random.randint(1, 7, 100),
    "transaction_volume": np.round(np.random.uniform(100, 1000, 100), 2),
    "employment_status": np.random.choice([0, 1], 100),
    "age": np.random.randint(21, 70, 100),
    "loan_amount": np.round(np.random.uniform(500, 5000, 100), 2),
    "previous_defaults": np.random.randint(0, 3, 100),
    "loan_default": np.random.choice([0, 1], 100)  # Target variable
}
df = pd.DataFrame(data)
df.to_csv("risk_data.csv", index=False)


Usage
Run the Risk Assessment Model
python main.py

Code Breakdown
1️⃣ Load Dataset
The script reads risk_data.csv, which contains features like credit score, social sentiment, and transaction volume.
2️⃣ Train-Test Split
The dataset is split into training (80%) and testing (20%) subsets.
3️⃣ Model Training
A Random Forest Classifier is trained to classify borrowers as high-risk (default) or low-risk (no default).
4️⃣ Model Evaluation
The trained model predicts outcomes and evaluates accuracy, precision, recall, and F1-score.

Future Improvements
Optimize Model: Use hyperparameter tuning (GridSearchCV)
Expand Features: Integrate behavioral analytics & alternative credit scoring
Real-Time Deployment: Convert the model into a web-based risk assessment API

