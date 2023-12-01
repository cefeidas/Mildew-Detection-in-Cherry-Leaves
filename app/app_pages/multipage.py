import streamlit as st


class MultiPage:
    """
    Class for multi-page Streamlit apps using object-oriented design.
    """

    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

    def add_page(self, title, func) -> None:
        """
        Add a new page to the app.
        :param title: Title of the page.
        :param func: Python function to render this page in Streamlit.
        """
        self.pages.append({"title": title, "function": func})

    def run(self):
        st.title(self.app_name)
        page = st.sidebar.radio('Navigation', self.pages,
                                format_func=lambda page: page['title'])

        # Running the selected page function
        page['function']()
