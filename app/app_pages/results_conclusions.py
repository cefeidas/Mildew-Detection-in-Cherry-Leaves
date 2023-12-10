import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Definir la ruta al directorio de test
test_dir = 'inputs/mildew_dataset/cherry-leaves/test'

# Parámetros de la imagen
img_width, img_height = 50, 50
batch_size = 20

# Crear un ImageDataGenerator para normalizar las imágenes
test_datagen = ImageDataGenerator(rescale=1./255)

# Crear el test_generator
test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary'
)

def display_page(app):
    st.title("Results and Conclusions")
    st.write("Explore outcomes and insights of the mildew project.")

    # Botón para evaluar el modelo
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