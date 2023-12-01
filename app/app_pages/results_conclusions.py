import streamlit as st


def display_page(app):
    st.title("Results and Conclusions")
    st.write("Explore the outcomes and insights from the mildew detection project.")
    col1, col2 = st.columns(2)
    if col1.button("Back"):
        app.previous_page()
