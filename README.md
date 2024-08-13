# Zaid Challenge Regression

Welcome to the Zaid Challenge Regression project! This educational project focuses on developing a comprehensive pipeline for property price prediction. Here’s a snapshot of what this project entails:

## Project Overview

In this project, we aim to create a user-friendly interface that allows individuals to estimate the price of a house based on various features. The project involves several key steps:

1. **Data Scraping and Cleaning**: We start by scraping property data and then clean the dataset to ensure high-quality inputs for our model.

2. **Feature Engineering**: We carefully select and engineer features to enhance the predictive power of our model. This includes handling missing values, encoding categorical variables, and selecting relevant features.

3. **Model Building**: We apply various regression techniques to build a robust model that predicts property prices. The performance of our models is evaluated to ensure accuracy.

4. **Streamlit Interface**: To make the predictions accessible to non-technical users, we develop an intuitive web interface using Streamlit. This allows users to input property details and receive price estimates easily.

## Features

- **Data Preprocessing**: Handles missing values and converts categorical data into numerical format.
- **Feature Selection**: Chooses the most relevant features for accurate predictions.
- **Model Evaluation**: Compares different regression models to identify the best-performing one.
- **Interactive Interface**: A Streamlit application where users can estimate house prices by entering property details.

## Getting Started

To explore the project, clone the repository and follow the instructions in the `Installation` section to set up the environment. Run the Streamlit app to start estimating property prices!

```bash
git clone https://github.com/yourusername/zaid-challenge-regression.git
cd zaid-challenge-regression
pip install -r requirements.txt
streamlit run app.py



-





## Data Preprocessing

### Dropped Columns
The following columns were dropped from the dataset:
- `url`
- `surfaceofplot`
- `gardenarea`
- `monthlycharges`
- `roomcount`
- `kitchen`

### Null Values Handling
The handling of null values is as follows:
- `constructionyear`: Filled with mean + outliers
- `bathroomcount`: Filled with median
- `garden`: Filled with 0
- `fireplace`: Filled with 0
- `floodingzone`: Filled with 'NON_FLOOD_ZONE'
- `peb`: Filled with mode
- `swimmingpool`: Filled with 0
- `numberoffacades`: Filled with median
- `livingarea`: Filled with median
- `terrace`: Filled with 0
- `toiletcount`: Filled with median
- `furnished`: Filled with 0

### String to Numerical Conversion
String features were converted to numerical values using `original_encoder`:
- `region`
- `district`
- `locality`
- `province`
- `stateofbuilding`
- `subtypeofproperty`

### Chosen Features
The following features were selected for the model:
- `bathroomcount`
- `bedroomcount`
- `swimmingpool`
- `subtypeofproperty_encoded`
- `numberoffacades`
- `garden`
- `terrace`
- `province_encoded`
- `furnished`
- `livingarea`
- `locality_encoded`
- `typeofproperty`
- `region_encoded`

## Model Performance
The performance of the models used in this project is summarized below:

- **Decision Tree Regressor**: 178,899.17
- **Gradient Boosting Regressor**: 162,194.12
- **Polynomial Features**: 188,592.61



