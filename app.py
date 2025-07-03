import streamlit as st 
import cv2
import numpy as np
from PIL import Image
import joblib
import time

col1, col2 = st.columns([1, 5])  

with col1:
    st.image("Dell_logo_2016.svg.png", width=200)

with col2:
    st.title("I'll Crack Your Head")
    
st.toast("Welcome Cutie Pie!", icon="🎉")
st.text("Crack Detector using KNN")
st.date_input("Transaction Date")
st.radio("Your department:",["Software Engineer","NPI","Test Engineer","Quality Engineer"])
model = joblib.load("trained_model_KNN.pkl")
st.snow()

# Preprocessing and feature extraction
def preprocess_image(img):
    blurred = cv2.GaussianBlur(img, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    return edges
 
def extract_features(img):
    resized = cv2.resize(img, (64, 64))
    return resized.flatten().reshape(1, -1)

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if uploaded_file != None:
    image = Image.open(uploaded_file).convert("L")
    img_array = np.array(image)
    
    st.image(image, caption="Succesfully Uploaded Image!")
    processed_image = preprocess_image(img_array)
    with st.spinner("Processing..."):
        time.sleep(3)
    features = extract_features(processed_image)
    
    prediction = model.predict(features)[0]
    label = "Positive" if prediction == 1 else "Negative"
    st.success(f"**Prediction:** {label}")
    st.balloons()
