import streamlit as st
import joblib

#Load the trained model 
model=joblib.load("news-classification-model.pkl")

#Define sentiment labels
news_labels={"0": "Technical", "1": "Business", "2" : "Sports", "3" : "Entertainment", "4" : "Politics"}


st.title("News classification")

#Input text area
user_input= st.text_area("Enter news here:")

#Pre
if st.button("Predict"):
    
    predicted_label=model.predict([user_input])[0]

    predicted_news_label=news_labels[str(predicted_label)]


    st.info(f"Predicted Sentiment: {predicted_news_label}")
