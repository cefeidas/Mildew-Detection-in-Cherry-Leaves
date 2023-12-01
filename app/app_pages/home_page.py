import streamlit as st


def display_page(app):
    st.title("Cherry Leaves Mildew Detection App")

    st.write("### Quick Project Overview")

    st.info(
        f"**General Information**\n"
        f"* Mildew in cherry leaves is a common fungal infection that affects the health and yield of cherry plantations.\n"
        f"* Early detection and treatment are crucial to prevent the spread of the disease and ensure a quality harvest.\n"
        f"* This app utilizes advanced image processing techniques to identify mildew presence in cherry leaves.\n\n"
        f"**Project Dataset**\n"
        f"* The dataset includes high-resolution images of cherry leaves, categorised into healthy and mildew-infected leaves.\n"
        f"* Each image has been meticulously annotated to aid in the accurate training of our detection models.")

    st.write(
        f"* For more information and to understand the dataset better, "
        f"please read the [Project Details](link_to_project_details).")

    st.success(
        f"The project focuses on 2 primary objectives:\n"
        f"* 1 - Conduct a study to visually differentiate between healthy and mildew-infected cherry leaves.\n"
        f"* 2 - Develop an efficient machine learning model to accurately predict mildew presence in cherry leaves.")

    # Insert an interactive or static image related to the project
    st.image("app/src/leaves.png",
             caption="Healthy vs Mildew Infected Cherry Leaves")
