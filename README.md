
# Parkinson's Disease Detection Model using SVM

## Overview

This project implements a machine learning model to detect Parkinson's Disease based on various voice features. The model uses Support Vector Machine (SVM) for classification after preprocessing the data with StandardScaler.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Files Included](#files-included)
- [Contributing](#contributing)
- [Credits](#credits)
- [License](#license)

## Introduction

Parkinson's Disease is a neurodegenerative disorder that affects movement. This project aims to predict the presence of Parkinson's Disease in individuals based on voice recordings using machine learning techniques. The model is trained on a dataset that includes various voice features extracted from clinical recordings.

Certainly! Here's how you can describe the features used in your Parkinson's Disease detection model in the README file:

---

## Features Used in Parkinson's Disease Detection Model

### MDVP Features
- **MDVP:Fo(Hz)**: Average vocal fundamental frequency.
- **MDVP:Fhi(Hz)**: Maximum vocal fundamental frequency.
- **MDVP:Flo(Hz)**: Minimum vocal fundamental frequency.

### Jitter Measures
- **MDVP:Jitter(%)**: Percentage measure of variation in fundamental frequency.
- **MDVP:Jitter(Abs)**: Absolute measure of variation in fundamental frequency.
- **MDVP:RAP**: Relative average perturbation, another measure of jitter.
- **MDVP:PPQ**: Five-point period perturbation quotient.
- **Jitter:DDP**: Average absolute difference of differences between consecutive periods.

### Shimmer Measures
- **MDVP:Shimmer**: Amplitude variation in the voice signal.
- **MDVP:Shimmer(dB)**: Amplitude variation in decibels.
- **Shimmer:APQ3**: Amplitude perturbation quotient 3.
- **Shimmer:APQ5**: Amplitude perturbation quotient 5.
- **MDVP:APQ**: Another measure of amplitude perturbation.
- **Shimmer:DDA**: Average absolute differences between amplitudes of consecutive periods.

### Other Measures
- **NHR**: Noise-to-Harmonics Ratio, a measure of noise in the voice signal.
- **HNR**: Harmonics-to-Noise Ratio, complementing NHR.

### Nonlinear Dynamical Complexity Measures
- **RPDE**: Recurrence Period Density Entropy.
- **D2**: Correlation dimension.

### Signal Fractal Scaling Exponent
- **DFA**: Detrended Fluctuation Analysis, indicating signal fractal scaling.

### Nonlinear Measures of Fundamental Frequency Variation
- **spread1**, **spread2**: Two nonlinear measures of fundamental frequency variation.
- **PPE**: Pitch Period Entropy, another measure of fundamental frequency variation.


---

This description provides a clear and concise overview of the features used in your model, helping users understand the inputs and their significance in predicting Parkinson's Disease. Adjust the descriptions as necessary based on your specific implementation and dataset details.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```
   git clone https://github.com/https://github.com/ajaysonwani/CodeClauseInternship_Parkinsons_desease_detection.git
   cd CodeClauseInternship_Parkinsons_desease_detection
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Download Required Files:**
   - Ensure you have the `scaler.pkl` and `model.pkl` files for scaling and the SVM model respectively. These files are required for prediction.

## Usage

1. **Run the Streamlit Application:**
   ```
   streamlit run app.py
   ```
   This will launch a Streamlit web application where you can input the voice features for prediction.

2. **Input Voice Features:**
   - Input the voice features in the provided fields.
   - Ensure all fields are filled with appropriate values.

3. **Get Prediction:**
   - Click on the "Is diagnosed with Parkinson's?" button to get the prediction result.
   - The application will display whether the individual is likely to have Parkinson's Disease based on the input features.
## Deployed Application

- Access the deployed application [here](https://parkinsons-disease-detection.streamlit.app/).

## Files Included

- **app.py**: Main application file containing the Streamlit interface and prediction logic.
- **scaler.pkl**: Pickled StandardScaler object used to scale input features.
- **model.pkl**: Pickled SVM model trained on voice features for Parkinson's Disease detection.
- **requirements.txt**: List of Python dependencies required to run the application.

