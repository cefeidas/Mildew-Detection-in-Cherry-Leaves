import streamlit as st


def display_page(app):
    st.title("Home")
    st.write("Welcome to the Cherry Leaves Mildew Detection App.")
    col1, col2 = st.columns(2)
    if col2.button("Next"):
        app.next_page()
