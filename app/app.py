from app_pages.multipage import MultiPage
import app_pages.page_home as home
import app_pages.page_project_introduction as project_intro
# Importa el resto de tus páginas aquí

# Crear una instancia de MultiPage
app = MultiPage("Cherry Leaves Mildew Detection App")

# Añadir páginas a la aplicación
app.add_page("Home", home.display_page)
app.add_page("Project Introduction", project_intro.display_page)
# Añadir el resto de tus páginas aquí

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run()
