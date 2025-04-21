# Credit Card Fraud Detection System

![Fraud Detection](https://img.shields.io/badge/Type-Machine%20Learning-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-brightgreen)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)

A machine learning-based web application for detecting fraudulent credit card transactions in real-time.

## Features

- 🚀 Real-time fraud detection for credit card transactions
- 📊 Interactive web interface built with Streamlit
- 🔍 Supports batch processing of transaction data via CSV upload
- 📥 Downloadable results with fraud probabilities
- ⚙️ Pre-trained model with feature scaling included

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8+
- pip package manager
- Virtual environment (recommended)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/credit-card-fraud-detection.git
   cd credit-card-fraud-detection

    Create and activate a virtual environment:
    bash

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required packages:
bash

    pip install -r requirements.txt

Usage

    Place your trained model files in the project directory:

        fraud_detection_model.pkl (the trained ML model)

        amount_scaler.pkl (the amount scaler)

    Run the Streamlit application:
    bash

    streamlit run app.py

    Access the web interface at http://localhost:8501

    Upload a CSV file containing transaction data with the following features:

        Transaction amount

        Other relevant features (V1-V28 for PCA components if using the standard credit card fraud dataset)

    Click "Detect Fraud" to get predictions

    Download the results with fraud predictions and probabilities

File Structure

credit-card-fraud-detection/
├── app.py                # Main Streamlit application
├── fraud_detection_model.pkl  # Pre-trained model
├── amount_scaler.pkl     # Feature scaler for amount
├── requirements.txt      # Python dependencies
├── README.md             # This file
└── sample_data/          # Sample transaction data (optional)

Model Details

The fraud detection system uses a pre-trained machine learning model with the following characteristics:

    Algorithm: [Specify your model type, e.g., Random Forest, XGBoost, etc.]

    Features: [List important features]

    Performance Metrics: [Include accuracy, precision, recall if known]

Sample Data Format

Your CSV file should contain transactions with the following format (adjust based on your model):
Time	V1	V2	...	V28	Amount
0	1.5	-0.5	...	0.2	100.00

Note: The actual features should match what your model was trained on.
Contributing

Contributions are welcome! Please follow these steps:

    Fork the project

    Create your feature branch (git checkout -b feature/AmazingFeature)

    Commit your changes (git commit -m 'Add some AmazingFeature')

    Push to the branch (git push origin feature/AmazingFeature)

    Open a Pull Request

License

Distributed under the MIT License. See LICENSE for more information.
