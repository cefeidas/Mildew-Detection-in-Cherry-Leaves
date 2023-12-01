import streamlit as st


def display_page(app):
    st.title("Model Interaction")
    st.write("Interact with the cherry leaves mildew detection model.")
    col1, col2 = st.columns(2)
    if col1.button("Back"):
        app.previous_page()
    if col2.button("Next"):
        app.next_page()
