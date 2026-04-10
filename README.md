Data Science Portfolio: Machine Learning & Geospatial Visualization

Overview
This repository contains two complementary data science projects demonstrating core competencies in **machine learning** and **geospatial data visualization** using Python. Together, they showcase the ability to work with structured datasets, build predictive models, and visualize real-world data interactively.


Author

AHABWE ARON



Project 1: Telco Customer Churn Prediction

 Description

This project implements a full machine learning pipeline to predict customer churn using the Telco Customer Churn dataset. 
It includes preprocessing, model training, evaluation, and feature importance analysis.

 Key Features

* Data loading and exploration (EDA)
* Data cleaning and preprocessing
* Categorical encoding using `LabelEncoder`
* Model training with:

  * Logistic Regression
  * Random Forest Classifier
  * K-Nearest Neighbors (KNN)
* Model evaluation using:

  * Classification reports
  * Confusion matrices
* Feature importance visualization (Random Forest)

 Workflow
1. Upload dataset (CSV)
2. Perform EDA (head, info, summary)
3. Preprocess data (handle missing values, encode categories)
4. Split into training and testing sets (80/20)
5. Train models
6. Evaluate performance
7. Visualize results

 Output
* Classification metrics for each model
* Confusion matrix plots
* Feature importance chart

 Limitations
* Assumes target column is `Churn`
* Uses basic encoding (LabelEncoder)
* No hyperparameter tuning


Project 2: Geospatial Earthquake Data Visualization

 Description
This project visualizes real-time earthquake data using geospatial techniques. It retrieves data from the USGS API and displays it on an interactive world map.

 Key Features
* Fetch real-time earthquake data (GeoJSON)
* Convert data into Pandas DataFrame
* Interactive map using Folium
* Depth-based color coding:

  * Green: Shallow (< 50 km)
  * Orange: Medium (50–150 km)
  * Red: Deep (> 150 km)
* Magnitude-based marker scaling
* Interactive popups with earthquake details
* Heatmap visualization of earthquake density

 Workflow
1. Fetch data from USGS API
2. Process and structure data
3. Create base map
4. Add markers and styling
5. Generate heatmap layer
6. Display summary statistics

 Output
* Interactive map with earthquake markers
* Heatmap of earthquake distribution
* Statistical summaries

 Limitations
* Data limited to recent timeframe (e.g., last 24 hours)
* Requires internet connection


 Technologies Used
* Python
* Pandas
* Scikit-learn
* Matplotlib
* Seaborn
* Folium
* Requests
* Branca
* Google Colab / Jupyter Notebook


Installation
Install all required dependencies:

```bash
pip install pandas scikit-learn matplotlib seaborn folium requests branca
```


How to Run

 Machine Learning Project
1. Open the Python script in Google Colab or local environment
2. Run the script
3. Upload the Telco dataset when prompted

 Geospatial Project
1. Open the Jupyter Notebook
2. Run all cells
3. View the interactive map output


 Possible Enhancements

 Machine Learning

* Hyperparameter tuning (GridSearchCV)
* Cross-validation
* Handling class imbalance (SMOTE)
* Model persistence (saving models)

Geospatial

* Time-based filtering (weekly/monthly data)
* Legend and UI controls
* Export map to HTML
* Animation of earthquake events over time


License
This repository is intended for educational and academic purposes.


Summary

This repository demonstrates:

* End-to-end machine learning pipeline development
* Real-world API data integration
* Interactive geospatial visualization
* Data analysis and interpretation skills

It serves as a practical showcase of applied data science techniques.
