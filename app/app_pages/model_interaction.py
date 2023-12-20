import streamlit as st

def display_page(app):
    st.title("Model Interaction")
    st.write("""
    ## Interact with the Cherry Leaves Mildew Detection Model

    We have developed a simple and user-friendly application that allows you to upload images of cherry leaves, either individually, in groups, or even as a ZIP file, to detect whether they are healthy or afflicted with powdery mildew.

    ### How to Use the Model:
    1. Access our specialized Jupyter Notebook designed for image analysis.
    2. Follow the instructions within the notebook to upload your cherry leaf images.
    3. The notebook will process the images and provide you with predictions.

    ### Get Started:
    To begin interacting with the model and analyze your cherry leaf images, please click on the link below to access our Jupyter Notebook:

    To launch the predictive model, follow the instructions in the README file.

    For the best experience, we recommend using a series of images that vary in appearance to see how our model performs across different scenarios.

    _Please note: The application is designed for educational and demonstration purposes and should not be used for critical decision-making in agricultural practices._
    """)

    st.write("For any additional information or queries, feel free to reach out to us through our contact page.")

# import streamlit as st
# from PIL import Image
# import numpy as np
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing.image import img_to_array
# import zipfile
# import io

# # Load the model once at the beginning
# model = load_model('cherry_leaf_cnn_model.h5')

# def display_page(app):
#     st.title("Model Interaction")
#     st.write("Interact with the cherry leaves mildew detection model.")

#     uploaded_files = st.file_uploader("Drag and Drop or Click to Upload Cherry Leaf Images or a ZIP file", type=['jpg', 'zip'], accept_multiple_files=True)

#     if uploaded_files is not None:
#         for uploaded_file in uploaded_files:
#             if uploaded_file.name.endswith('.zip'):
#                 # Process images inside a ZIP file
#                 with zipfile.ZipFile(uploaded_file, 'r') as zip_ref:
#                     for file_name in zip_ref.namelist():
#                         image_data = zip_ref.read(file_name)
#                         process_and_display_image(image_data)
#             else:
#                 # Process a single image
#                 image_data = uploaded_file.getvalue()
#                 process_and_display_image(image_data)
#     else:
#         st.write("Please upload JPG images or a ZIP file.")

# def process_and_display_image(image_data):
#     # Convert to PIL object
#     image = Image.open(io.BytesIO(image_data))
#     # Resize and prepare the image
#     image = prepare_image(image)
#     # Display image and prediction
#     st.image(image, caption='Uploaded Cherry Leaf', use_column_width=True)
#     predict_and_display(image)

# def prepare_image(image):
#     image = image.resize((50, 50))
#     return img_to_array(image) / 255.0

# def predict_and_display(image):
#     image = np.expand_dims(image, axis=0)
#     prediction = model.predict(image)
#     label = 'Healthy' if prediction < 0.5 else 'Powdery Mildew'
#     st.write(f'Prediction: {label}')

# # Call the display_page function from your main application
# # display_page(app)
