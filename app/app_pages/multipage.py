import streamlit as st


class MultiPage:
    """
    Class to generate multiple Streamlit pages using an object oriented approach.
    """

    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
            page_title=self.app_name,
            page_icon="🌿")  # Custom icon for your app, related to cherry leaves

    def add_page(self, title, func) -> None:
        """
        Add a new page to the app.
        :param title: Title of the page.
        :param func: Python function to render this page in Streamlit.
        """
        self.pages.append({"title": title, "function": func})

    def run(self):
        """
        Run the app and display the pages in the sidebar menu.
        """
        st.title(self.app_name)
        # Creating a sidebar for navigation
        page = st.sidebar.radio('Navigation', self.pages,
                                format_func=lambda page: page['title'])

        # Running the selected page function
        page['function']()


app = MultiPage("Cherry Leaves Mildew Detection App")

# Adding pages to the app
app.add_page("Home", home_page.display_page)
app.add_page("Project Introduction", project_introduction.display_page)
app.add_page("Model Interaction", model_interaction.display_page)
app.add_page("Results and Conclusions", results_conclusions.display_page)

if __name__ == "__main__":
    app.run()
