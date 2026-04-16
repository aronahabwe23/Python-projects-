# -*- coding: utf-8 -*-
"""ASSIGNMENT 3...MACHINE LEARNING WITH Scikit



Original file is located at
    https://colab.research.google.com/drive/1VMOTpZrfgNQbw4DBP2_JmZXW9KIVFz2g
"""

# Install required libraries
!pip install --quiet pandas scikit-learn matplotlib seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay

from google.colab import files

# Machine Learning with Scikit-learn
# By AHABWE ARON


# Step 1: Upload Dataset (Telco Customer Churn CSV)
print("Please upload the Telco Customer Churn dataset (CSV file).")
uploaded = files.upload()

# Load dataset into pandas DataFrame
filename = list(uploaded.keys())[0]
df = pd.read_csv(filename)

# Step 2: Exploratory Data Analysis
print("\nFirst 5 rows of the dataset:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nDataset Summary:")
print(df.describe())

# Step 3: Preprocess Data
# Handle missing values
df = df.dropna()

# Encode categorical variables using LabelEncoder
label_encoders = {}
for column in df.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le

# Step 4: Split data into features (X) and target (y)
X = df.drop("Churn", axis=1)  # Assuming target column is 'Churn'
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train three models
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "KNN": KNeighborsClassifier(n_neighbors=5)
}

for name, model in models.items():
    print(f"\nTraining {name}...")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print(f"\n{name} Classification Report:")
    print(classification_report(y_test, y_pred))

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot(cmap="Blues")
    plt.title(f"{name} - Confusion Matrix")
    plt.show()

# Step 6: Feature Importance (for Random Forest)
rf_model = models["Random Forest"]
importances = rf_model.feature_importances_
features = X.columns

plt.figure(figsize=(10, 5))
sns.barplot(x=importances, y=features)
plt.title("Feature Importance (Random Forest)")
plt.xlabel("Importance Score")
plt.ylabel("Features")
plt.tight_layout()
plt.show()
