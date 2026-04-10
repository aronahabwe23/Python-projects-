 Telco Customer Churn Prediction (Scikit-learn)

 Overview

This project implements a complete machine learning workflow using **Scikit-learn** to predict customer churn from the Telco Customer Churn dataset. 
It covers data loading, preprocessing, exploratory data analysis (EDA), model training, evaluation, and feature importance visualization.

Author;

AHABWE ARON

 Features

* Upload and load a CSV dataset
* Perform basic exploratory data analysis (EDA)
* Handle missing values
* Encode categorical variables using `LabelEncoder`
* Train multiple machine learning models:

  * Logistic Regression
  * Random Forest Classifier
  * K-Nearest Neighbors (KNN)
* Evaluate models using:

  * Classification report (precision, recall, F1-score)
  * Confusion matrix visualization
* Visualize feature importance (Random Forest)

 Technologies Used

* Python
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* Google Colab (for execution)

 Installation

Install required dependencies:

```bash
pip install pandas scikit-learn matplotlib seaborn
```

 Dataset

The project expects the **Telco Customer Churn dataset (CSV format)**.

  Ensure the dataset contains a column named `Churn` (target variable).
  All categorical columns will be automatically encoded.

How to Run

1. Open the script in **Google Colab** or a Python environment.
2. Run the script.
3. Upload the Telco Customer Churn CSV file when prompted.
4. The script will:

   * Display dataset information
   * Preprocess the data
   * Train models
   * Output evaluation metrics
   * Display visualizations

 Project Workflow

1. Data Upload & Loading
   User uploads dataset via Colab interface

2. Exploratory Data Analysis (EDA)
   View dataset structure and summary statistics

3. Data Preprocessing
 Remove missing values
 Encode categorical variables

4. Train-Test Split
 80% training, 20% testing

5. Model Training**
     Logistic Regression
     Random Forest
     KNN

6. Model Evaluation

    Classification reports
    Confusion matrices
7. Feature Importance Analysis**

Random Forest feature importance visualization

 Output

 Printed classification reports for each model
 Confusion matrix plots
 Feature importance bar chart

Notes / Limitations

Assumes target column is named `Churn`
  Uses simple label encoding (may not be optimal for all categorical data)
  Drops missing values instead of imputing them
  No hyperparameter tuning is performed

 Possible Improvements

 Use `OneHotEncoder` instead of `LabelEncoder`
 Add hyperparameter tuning (GridSearchCV / RandomizedSearchCV)
 Implement cross-validation
 Handle class imbalance (SMOTE, class weights)
 Save trained models
 Build a simple UI or API for predictions

 License

This project is for educational and practice purposes.
