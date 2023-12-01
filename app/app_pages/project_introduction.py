import streamlit as st


def display_page(app):
    st.title("Project Introduction")
    st.write("This page introduces the project for detecting mildew in cherry leaves.")
    col1, col2 = st.columns(2)
    if col1.button("Back"):
        app.previous_page()
    if col2.button("Next"):
        app.next_page()
