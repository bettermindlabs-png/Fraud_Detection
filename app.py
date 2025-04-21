import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load model and scaler
model = joblib.load('fraud_detection_model.pkl')
scaler = joblib.load('amount_scaler.pkl')

st.set_page_config(page_title="Fraud Detection", layout="wide")
st.title("💳 Credit Card Fraud Detection")

uploaded_file = st.file_uploader("Upload transaction data (CSV)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    # Preprocess Amount
    if 'Amount' in df.columns:
        df['Amount'] = scaler.transform(df['Amount'].values.reshape(-1, 1))
    
    st.write("### Sample Data", df.head())
    
    if st.button("Detect Fraud"):
        # Predict
        predictions = model.predict(df)
        probabilities = model.predict_proba(df)[:, 1]
        
        # Add results
        df['Prediction'] = ['Fraud' if x == 1 else 'Legitimate' for x in predictions]
        df['Fraud Probability'] = probabilities
        
        st.write("### Results")
        st.dataframe(df)
        
        # Download results
        st.download_button(
            label="Download Predictions",
            data=df.to_csv(index=False),
            file_name='fraud_predictions.csv',
            mime='text/csv'
        )
