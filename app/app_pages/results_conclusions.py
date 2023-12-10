import streamlit as st
from tensorflow.keras.models import load_model


def display_page(app):
    st.title("Results and Conclusions")
    st.write("Explore outcomes and insights of the mildew project.")

    # Button to evaluate the model
    if st.button('Evaluate Model'):
        model = load_model('cherry_leaf_cnn_model.h5')
        evaluation_score = model.evaluate(test_generator)
        accuracy = evaluation_score[1]
        st.write(f"Model Accuracy: {accuracy:.2f}")

    # Information about the model evaluation
    st.info(
        "**Model Evaluation**\n"
        "* Model Accuracy: Approximately 98%.\n"
        "* Industrial Benchmark: The industry standard for such tools is generally lower.\n"
        "* Conclusion: Our model significantly surpasses reliability benchmarks, indicating high confidence in its predictions."
    )

    # Information about the initial hypothesis and its validation
    st.info(
        "**Hypothesis Validation**\n"
        "* Initial Hypothesis: Visible differences between healthy and mildew-infected cherry leaves can be detected by a CNN.\n"
        "* With the high accuracy achieved, we consider the initial hypothesis validated.\n"
        "* Our CNN model successfully differentiates between the two categories, mimicking human visual perception."
)