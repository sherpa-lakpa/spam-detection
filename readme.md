# Email Spam or Ham Classifier

This project involves building a machine learning model to classify emails as spam or ham (non-spam). The dataset used for training and evaluation is available on [Kaggle](https://www.kaggle.com/datasets/bilaliqbalai/spam-ham-dataset).

[Liv Preview](https://spam-detection-ihty.onrender.com/).

## Overview

The goal of this project is to develop a reliable email classifier using natural language processing and machine learning techniques. The project includes data cleaning, exploratory data analysis (EDA), feature engineering, model selection, hyperparameter tuning, and model evaluation.

## Project Structure

The project structure includes the following key components:

- **Data Cleaning:** Handling missing values and ensuring the dataset is clean.

- **Exploratory Data Analysis (EDA):** Analyzing the dataset to gain insights into the distribution of spam and ham messages, text lengths, and other relevant characteristics.

- **Feature Engineering:** Creating a text processing function to clean and prepare textual data for modeling.

- **Model Selection:** Building pipelines for three different classifiers - Multinomial Naive Bayes, Random Forest, and Support Vector Classifier (SVC).

- **Hyperparameter Tuning:** Using GridSearchCV to find the best hyperparameters for the SVC model.

- **Model Evaluation:** Evaluating the models' performance using accuracy scores, confusion matrices, and classification reports.

- **Flask Web App:** Developing a Flask web application for user interaction and real-time predictions.

- **Deployment:** Deploying the trained model and web app.

## Getting Started

To run the project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/sherpa-lakpa/spam-detection.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run the Flask web app: `python app.py`

## Model Deployment

The trained model is saved using the `joblib` library and can be deployed in a production environment. The Flask web app provides a user interface for making predictions on new input.

## Project Collaboration

This project involves collaboration between Pradeep and Lakpa. Task distribution and responsibilities are outlined in the table below:

| Task                       | Pradeep                  | Lakpa                    |
|----------------------------|--------------------------|--------------------------|
| Data Cleaning              | Data Cleaning            |                          |
| EDA and Visualization      | EDA and Visualization    |                          |
| Feature Engineering        | Feature Engineering      |                          |
| Model Evaluation           | Model Evaluation         |                          |
| Model Selection            |                          | Model Selection          |
| Pipeline Building          |                          | Pipeline Building        |
| Hyperparameter Tuning      |                          | Hyperparameter Tuning    |
| Flask Web App Development   |                          | Flask Web App Development|
| Deployment                 | Deployment               | Deployment               |

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to contribute, report issues, or suggest improvements!
