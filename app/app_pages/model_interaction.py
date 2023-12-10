import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

def display_page(app):
    st.title("Model Interaction")
    st.write("Interact with the cherry leaves mildew detection model.")

    uploaded_files = st.file_uploader("Drag and Drop or Click to Upload Cherry Leaf Images or a ZIP file", type=['jpg', 'zip'], accept_multiple_files=True)

    if uploaded_files is not None:
        for uploaded_file in uploaded_files:
            # Read the image and convert it into a PIL object
            image = Image.open(uploaded_file)
            
            # Resize the image to 50x50 pixels
            image = image.resize((50, 50))
            
            # Convert the image to an array and normalize it
            image = img_to_array(image) / 255.0
            image = np.expand_dims(image, axis=0)  # Expand dimensions for the model

            # Load the model
            model = load_model('cherry_leaf_cnn_model.h5')

            # Make the prediction
            prediction = model.predict(image)
            label = 'Healthy' if prediction < 0.5 else 'Powdery Mildew'

            # Display the image and the prediction
            st.image(image, caption='Uploaded Cherry Leaf', use_column_width=True)
            st.write(f'Prediction: {label}')
    else:
        st.write("Please upload JPG images or a ZIP file.")



