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

    [Go to Jupyter Notebook for Cherry Leaves Analysis](<Link_to_your_Jupyter_Notebook>)

    For the best experience, we recommend using a series of images that vary in appearance to see how our model performs across different scenarios.

    _Please note: The application is designed for educational and demonstration purposes and should not be used for critical decision-making in agricultural practices._
    """)

    st.write("For any additional information or queries, feel free to reach out to us through our contact page.")




