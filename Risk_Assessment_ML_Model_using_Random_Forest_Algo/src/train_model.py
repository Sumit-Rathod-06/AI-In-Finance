import pandas as pd
import numpy as np
import pickle
import os
import warnings
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from imblearn.over_sampling import SMOTE
from preprocess import load_and_clean_data

warnings.simplefilter(action='ignore', category=FutureWarning)

df = load_and_clean_data(r"C:\Users\HP\Desktop\AiF\AI-In-Finance\Risk_Assessment_ML_Model_using_Random_Forest_Algo\data\dataset.csv")

X = df.drop(columns=['repay_fail'])
y = df['repay_fail']
y = y.astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

param_dist = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5, 10],
}

random_search = RandomizedSearchCV(
    RandomForestClassifier(random_state=42),
    param_distributions=param_dist,
    n_iter=10,  
    cv=3,
    scoring='accuracy',
    n_jobs=-1,  
)

random_search.fit(X_train, y_train)

best_model = random_search.best_estimator_

best_model.fit(X_train, y_train)

y_pred = best_model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

os.makedirs("../models", exist_ok=True)
with open("../models/credit_model.pkl", "wb") as f:
    pickle.dump(best_model, f)

print("Model saved successfully!")
