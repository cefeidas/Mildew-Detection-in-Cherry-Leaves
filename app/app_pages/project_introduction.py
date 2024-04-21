import streamlit as st


def display_page():
    st.title("Project Introduction")
    st.write("This page outlines the project on cherry leaf mildew detection.")

    st.info(
    "**Project Overview**\n"
    "* Objective: Identify mildew in cherry leaves using a CNN.\n"
    "* Why: Mildew affects cherry crop health and yield.\n"
    "* Approach: Use a CNN for autonomous pattern recognition.\n"
    "* Data: Large dataset of images of cherry leaves.\n"
    "* Classification: Healthy vs. Mildew-infected leaves.\n"
    "* Note: CNN mimics human visual perception, no mathematical analysis of images.\n"
    "* Hypothesis: Visible differences to humans should be detectable by CNN."
)

st.write(
        f"* For more information and to understand the dataset better, "
        f"please read the [Project Details](link_to_project_details).")
