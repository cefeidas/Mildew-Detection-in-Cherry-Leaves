import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def display_page(app):
    st.title("Results and Conclusions")
    st.write("Explore outcomes and insights of the mildew project.")


    # Information about the model evaluation
    st.info(
        "**Model Evaluation**\n"
        "* Model Accuracy: Approximately 99.83% (rounded to 1.00 when evaluated).\n"
        "* Industry Benchmark: Commonly, a score above 95% is considered good in the industry.\n"
        "* Conclusion: Our model significantly surpasses reliability benchmarks, indicating high confidence in its predictions."
    )

    # Information about the initial hypothesis and its validation
    st.info(
        "**Hypothesis Validation**\n"
        "* Initial Hypothesis: Visible differences between healthy and mildew-infected cherry leaves can be detected by a CNN.\n"
        "* With the high accuracy achieved, we consider the initial hypothesis validated.\n"
        "* Our CNN model successfully differentiates between the two categories, mimicking human visual perception."
)