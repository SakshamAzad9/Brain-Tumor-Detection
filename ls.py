import streamlit as st
from ultralytics import YOLO
from PIL import Image
import matplotlib.pyplot as plt
import numpy as npz

# Streamlit app title
st.title("Brain Tumor Detection with YOLO")

# Load YOLO model
model_path = r'C:\Users\saksh\Test1\runs\detect\train\weights\best.pt'
trained_model = YOLO(model_path)

# Image upload option
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    
    # Run the model on the uploaded image
    image = Image.open(uploaded_file)
    results = trained_model(image)
    
    # Process and display the results
    result_image = results[0].plot()  # Assuming results[0].plot() returns a displayable array

    # Convert the result image to an RGB image
    result_image_rgb = Image.fromarray(result_image.astype("uint8"), "RGB")
    
    st.image(result_image_rgb, caption="Detected Results", use_column_width=True)

    # Show model results in a textual format if desired
    st.write("Detection results:")
    for result in results:
        st.write(result)
