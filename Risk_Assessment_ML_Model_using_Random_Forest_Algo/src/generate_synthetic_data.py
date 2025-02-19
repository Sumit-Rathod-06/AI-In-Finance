import pandas as pd
import numpy as np
import os

def generate_synthetic_data(file_path="../data/dataset.csv", num_samples=1000):
    np.random.seed(42)

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    data = {
        'income': np.random.randint(10000, 100000, num_samples),  
        'spending_habit': np.random.uniform(0.1, 1.0, num_samples),  
        'social_media_score': np.random.randint(300, 900, num_samples),  
        'transaction_frequency': np.random.randint(1, 50, num_samples),  
        'credit_history': np.random.randint(0, 2, num_samples),  
        'loan_amount': np.random.randint(500, 50000, num_samples),  
        'credit_utilization': np.random.uniform(0.1, 1.0, num_samples),  
    }

    df = pd.DataFrame(data)

    df['loan_default'] = np.tile([0, 1], num_samples // 2)  

    df.to_csv(file_path, index=False)
    print(f"✅ Synthetic dataset generated and saved to {file_path}")

if __name__ == "__main__":
    generate_synthetic_data()
