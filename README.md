# Heart Failure Prediction Using Machine Learning

This project provides a complete pipeline to predict heart failure clinical events using machine learning, from training in Google Colab to deploying as a web app with Flask.

![Project Screenshot]<img width="324" height="580" alt="image" src="https://github.com/user-attachments/assets/b977e022-1644-4272-9082-02a29634d9b3" />


---

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Project Workflow](#project-workflow)
- [Model Training](#model-training)
- [Web Application](#web-application)
- [How to Run](#how-to-run)
- [File Structure](#file-structure)
- [Results](#results)
- [References](#references)

---

## Introduction

Heart failure is a leading global health concern. Early and accurate prediction can help in timely intervention and better patient outcomes. This project applies a RandomForestClassifier to a real-world heart failure dataset to predict the likelihood of a death event in patients.

## Dataset

The project uses the Heart Failure Clinical Records Dataset from the UCI Machine Learning Repository. This dataset consists of 299 patients and captures clinical data and outcomes over time.

Features include:
- Age, sex, blood test results, presence of comorbidities (e.g., anaemia, diabetes), and follow-up period.
- Outcome variable: DEATH_EVENT (1 = event, 0 = no event).

## Project Workflow

1. Data Exploration & Preprocessing:  
   - The dataset is loaded and split into training/testing sets (using scikit-learn).
   - Missing values and outliers are checked/handled as appropriate.
2. Model Training:  
   - A RandomForestClassifier is trained with the training data.
   - Model accuracy and performance are evaluated (as shown in the photo, achieving ~73% test accuracy[1]).
   - The trained model is saved as model.pkl with pickle.
3. Deployment:  
   - The saved model is deployed using a minimal Flask web application.
   - The web app provides an HTML form for user input and returns a prediction.
4. Final Integration:  
   - All files are arranged in a modular structure for easy deployment.

## Model Training

- Implemented in a Google Colab notebook for accessibility and reproducibility.
- Key steps:
- from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
from sklearn.metrics import accuracy_score
print("accuracy:", accuracy_score(y_test, y_pred))
- Test Accuracy:  
~73% (as shown in the Colab output above[1]).

## Web Application

- Framework: Flask (Python)
- Files:
- app.py: Loads model.pkl and serves a prediction via a web form.
- templates/index.html: User interface for entering patient data and displaying results.
- Prediction Logic:  
User inputs required features; Flask processes them, loads the model, and returns the result ("Survived" or "Death Event").

## How to Run

1. Clone the repository:
2. 
