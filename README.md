# Mildew Detection in Cherry Leaves

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation and Setup](#installation-and-setup)
- [Design and User Stories](#design-and-user-stories)
- [Data Analysis and Model Development](#data-analysis-and-model-development)
- [Testing](#testing)
- [Credits](#credits)
- [License](#license)
- [Conclusion](#conclusion)


## Introduction

This project focuses on developing a machine learning model to distinguish healthy cherry leaves from those affected by powdery mildew. The goal is to create a system that quickly and accurately identifies affected leaves, aiding in early disease management and prevention.

## Prerequisites

This project is organized into two primary parts: the Jupyter Notebooks for in-depth analysis and model development, and the Mildew Detection App, which also serves as an interactive dashboard for a non-technical audience. Below are the prerequisites for engaging with each component.

### Mildew Detection App (Interactive Dashboard)

To effectively use the Mildew Detection App and its dashboard functionality, the following are required:

- **Web Browser**: Compatible with modern browsers such as Chrome, Firefox, Safari, or Edge for optimal experience.
- **Internet Connection**: Essential for accessing the app and its features.
- **Image Formats**: Ability to upload images in JPEG, PNG, or other common formats for analysis.

#### Accessing the Mildew Detection Dashboard

The interactive Mildew Detection Dashboard is hosted on Heroku, providing an easy and direct way to interact with our model. You can access the dashboard using the following link:

[Heroku Dashboard Link](https://your-heroku-app-link.com)

No installation or setup is required to use the dashboard. It's designed to be user-friendly, allowing you to upload cherry leaf images and get instant predictions on their health status.


### Jupyter Notebooks

The Jupyter Notebooks are crucial for the technical aspects of this project, including data processing and model training. Ensure you have the following setup:

- **Python 3.x**: Install Python from [Python.org](https://www.python.org/downloads/).
- **Jupyter Notebook**: Installation instructions available on [Jupyter.org](https://jupyter.org/install).
- **Python Libraries**: Necessary libraries such as TensorFlow, NumPy, Pandas, Matplotlib, Seaborn, and Keras, can be installed from the `requirements.txt` file.
- **Dataset**: Access to the cherry leaves dataset is required for model training and evaluation.

#### Launching Jupyter Notebooks

Once Jupyter Notebook is installed, you can launch it to interact with the project's detailed analysis and model development notebooks. Follow these simple steps:

1. Open your command line interface (CLI).
2. Navigate to the directory where your Jupyter Notebooks are located.
3. Run the following command to start Jupyter Notebook:
  jupyter notebook --NotebookApp.token='' --NotebookApp.password=''
4. This command will open Jupyter Notebook in your default web browser.
5. From the Jupyter interface, you can open and run individual notebooks to explore the project's analysis and models.

Note: The `--NotebookApp.token='' --NotebookApp.password=''` flags are optional and are used to disable the token and password for ease of access. It's recommended to use these flags only in a secure and trusted environment.

### Python Library Versions

The project has been developed with specific library versions to ensure compatibility. Install these libraries as per the `requirements.txt` file in the repository. Key libraries and their versions include:

- `numpy==1.19.2`
- `pandas==1.1.2`
- `matplotlib==3.3.1`
- `seaborn==0.11.0`
- `plotly==4.12.0`
- `streamlit==0.85.0`
- `scikit-learn==0.24.2`
- `tensorflow-cpu==2.6.0`
- `keras==2.6.0`
- `protobuf==3.20`
- `altair<5`

Run `pip install -r requirements.txt` in your project environment to install these dependencies.

## Installation and Setup

Instructions on setting up the project environment, including:

- Cloning the GitHub repository
- Installing necessary Python libraries
- Setting up the Jupyter Notebook environment
- Follow the Jupyter Notebooks step by step for accessing and preparing the cherry leaves dataset

## Design and User Stories

This project's design is intricately tied to the enhanced user stories that guide its development. Below is an overview of how each user story has influenced the project's design and functionality:

### Project Initiation with README Documentation

- **Priority**: Must Have (10%)
- **Implementation**: The project begins with a detailed README file, outlining the project's goals, structure, and technology usage, and is regularly updated to reflect the project's evolution.

### Cherry Leaf Data Acquisition and Preparation

- **Priority**: Must Have (10%)
- **Implementation**: The project involves the collection and preprocessing of cherry leaf images, preparing them for effective model training and accurate predictions.

### Optimizing Image Resolution for Data Processing

- **Priority**: Must Have (10%)
- **Implementation**: High-resolution cherry leaf images are resized to smaller dimensions, optimizing them for efficient data processing and CPU usage.

### Initial Data Exploration with Jupyter Notebooks

- **Priority**: Must Have (10%)
- **Implementation**: Early exploratory data analysis is conducted in Jupyter Notebooks, providing insights into the dataset and informing the model development.

### Ongoing Code Testing and Documentation

- **Priority**: Should Have (20%)
- **Implementation**: The development process includes regular documentation and code testing within Jupyter Notebooks to maintain the quality and reliability of the code and models.

### Structured Model Development Lifecycle

- **Priority**: Must Have (10%)
- **Implementation**: The model development process is segmented into training, validation, and evaluation phases, ensuring accurate performance assessment and model refinement.

### Interactive Dashboard Development for Data Visualization

- **Priority**: Should Have (20%)
- **Implementation**: An interactive dashboard is developed to visually present the project's findings, progress, and model predictions in an engaging and user-friendly manner.

### Comprehensive Project Review and Enhancement

- **Priority**: Could Have (10%)
- **Implementation**: The project undergoes a thorough final review, focusing on iterative improvements to meet all objectives and standards.

### Finalizing and Updating Project Documentation

- **Priority**: Could Have (10%)
- **Implementation**: The project concludes with a comprehensive update to the README file, summarizing the project’s achievements, challenges, and key learnings.

### Incorporation of Advanced Visual Analysis for Enhanced Insights

- **Priority**: Nice to Have
- **Implementation**: The project explores integrating advanced visual analysis tools for analyzing model performance graphs, to provide deeper insights into model accuracy and efficiency.

Each of these user stories has been carefully considered to ensure the project meets its intended goals and provides a meaningful and functional outcome for its users.

## Data Analysis and Model Development

### Exploratory Data Analysis

The exploratory data analysis for this project focused on understanding the fundamental characteristics of the cherry leaves dataset. However, it's important to note that the nature of Convolutional Neural Networks (CNN) limits the need for extensive pre-analysis. CNNs autonomously identify patterns and critical features in the dataset without relying on pre-drawn conclusions or mathematical analysis of image differences.

### Model Training and Evaluation

The Machine Learning model used in this project is a CNN, designed to classify cherry leaves as healthy or infected with powdery mildew. The dataset was divided into training (70%), validation (20%), and testing (10%) sets. The training phase involved exposing the CNN to various images, allowing it to learn distinguishing features. The validation phase helped in tuning the model parameters, while the testing phase evaluated the model's performance. The model's accuracy and other performance metrics were closely monitored to ensure reliable predictions.

### Dashboard Development

The development of the dashboard was tailored to be interactive and user-friendly, focusing primarily on facilitating image upload and analysis. Due to the 'black box' nature of CNNs, extensive data analysis before or after model training is not particularly beneficial. In a CNN, layers of neurons automatically and adaptively learn spatial hierarchies of features from the input images. This means that the model self-determines the most relevant features for classification without human intervention or insight.

This 'black box' characteristic of CNNs implies that the model does not reveal which specific features it uses to make predictions. Therefore, post-hoc data analysis would not provide additional insight into the model's decision-making process. As a result, the dashboard was designed with a minimalist approach, focusing on the core functionality of uploading images and displaying the model's predictions. This design choice reflects the autonomous learning and analysis capabilities of CNNs, which are central to the project's objective of accurately identifying powdery mildew in cherry leaves.

## Testing

### **Multi-Page Dashboard Test Cases**

### Test Case 1: Page Navigation
- **Objective**: Ensure seamless navigation between different pages of the dashboard.
- **Procedure**:
  1. Open the dashboard.
  2. Click on each menu item to navigate to different pages.
  3. Ensure that the correct page is displayed each time.
- **Expected Result**: Each page should load correctly without errors.

### Test Case 2: Data Visualization Accuracy
- **Objective**: Verify that all data visualizations display accurate and up-to-date information.
- **Procedure**:
  1. Navigate to each page containing data visualizations.
  2. Cross-reference displayed data with known data sources for accuracy.
- **Expected Result**: All charts and graphs accurately represent the data source.

### Test Case 3: Interactive Elements
- **Objective**: Test all interactive elements like buttons, sliders, or dropdowns for functionality.
- **Procedure**:
  1. Identify all interactive elements on each page.
  2. Interact with each element to ensure they are functional.
- **Expected Result**: All interactive elements should work as intended.

### Test Case 4: Responsiveness and Layout Integrity
- **Objective**: Ensure the dashboard is responsive and maintains layout integrity across different devices and browsers.
- **Procedure**:
  1. Open the dashboard in various browsers (Chrome, Firefox, Safari).
  2. Resize the browser window and access the dashboard on different devices (desktop, tablet, mobile).
- **Expected Result**: The dashboard should be responsive with consistent layout and functionality.

### Test Case 5: Error Handling
- **Objective**: Test the dashboard's ability to handle errors gracefully.
- **Procedure**:
  1. Simulate common user errors (e.g., incomplete form submissions, broken links).
  2. Observe the dashboard's response.
- **Expected Result**: The dashboard should display appropriate error messages without crashing.

### Test Case 6: Data Loading and Performance
- **Objective**: Ensure data loads efficiently and dashboard performance is optimal.
- **Procedure**:
  1. Monitor load times for pages and visualizations.
  2. Check for any performance lags or delays.
- **Expected Result**: Data should load within a reasonable time frame, and the dashboard should perform smoothly.

### **Jupyter Notebook Test Cases**

### Test Case 1: Code Execution
- **Objective**: Ensure all cells in the notebook run without errors.
- **Procedure**:
  1. Run each cell in the notebook sequentially.
  2. Observe for any errors or exceptions.
- **Expected Result**: All cells should execute successfully, producing expected outputs.

### Test Case 2: Data Processing Accuracy
- **Objective**: Verify the accuracy of data processing steps.
- **Procedure**:
  1. Review data cleaning, transformation, and analysis steps.
  2. Cross-verify with expected outcomes or known benchmarks.
- **Expected Result**: Data processing steps should yield accurate and logical results.

### Test Case 3: Model Performance Metrics
- **Objective**: Test the accuracy and reliability of machine learning models.
- **Procedure**:
  1. Review the model performance metrics in the notebook.
  2. Compare against predefined thresholds or benchmarks.
- **Expected Result**: Model metrics (e.g., accuracy, precision, recall) should meet or exceed set standards.

### Test Case 4: Reproducibility
- **Objective**: Ensure results are reproducible.
- **Procedure**:
  1. Restart the notebook kernel and clear outputs.
  2. Re-run all cells and compare results to previous runs.
- **Expected Result**: Results should be consistent across multiple runs.

### Test Case 5: Visualization Effectiveness
- **Objective**: Test the effectiveness and accuracy of data visualizations.
- **Procedure**:
  1. Review all plots and charts in the notebook.
  2. Check for correct representation of data and clarity in conveying insights.
- **Expected Result**: Visualizations should accurately represent data and aid in interpretation.

### Test Case 6: Documentation and Comments
- **Objective**: Ensure that the notebook is well-documented with clear explanations and comments.
- **Procedure**:
  1. Read through the documentation and comments in the notebook.
  2. Check for clarity, completeness, and relevance.
- **Expected Result**: The notebook should have comprehensive and clear documentation and comments.

## Deployment
A detailed guide to deploying the Streamlit dashboard on Heroku:

### Step 1: Prepare the Application
- Ensure all dependencies are listed in the `requirements.txt` file.
- Create a `setup.sh` file for Streamlit configuration on Heroku.
- Include a `runtime.txt` file to set the Python environment to version 3.8.12.

### Step 2: Set Up Heroku
- Create a Heroku account if you don't have one.
- In your Heroku dashboard, create a new application.

### Step 3: Connect to GitHub
- In the Heroku app settings, connect to your GitHub repository.
- Choose the option to deploy manually or enable automatic deployment.
  - It is recommended to keep automatic deployments disabled for untested changes.
- Select the branch to deploy and click the "Deploy Branch" button.

### Step 4: Monitor the Build
- Keep an eye on the build log during deployment.
- Resolve any errors that may occur to ensure a smooth build process.

### Step 5: Access Your Live Application
- Once deployed, Heroku will provide a public URL.
- Visit the URL to see your Streamlit dashboard running live.

### Conclusion
Congratulations on deploying your Streamlit dashboard on Heroku. This completes the process from development to live deployment, providing a public-facing ML application.

### Next Steps
- Continue enhancing your application based on user feedback.
- Explore additional features or datasets for future updates.

## Credits

This project utilizes a range of libraries, each contributing to different aspects of the machine learning pipeline and dashboard development:

- **NumPy (1.19.2)**: Essential for scientific computing in Python. [NumPy Documentation](https://numpy.org/doc/1.19/).
- **Pandas (1.1.2)**: Provides powerful data structures and data analysis tools. [Pandas Documentation](https://pandas.pydata.org/pandas-docs/version/1.1.2/).
- **Matplotlib (3.3.1)**: A comprehensive library for creating static, animated, and interactive visualizations. [Matplotlib Documentation](https://matplotlib.org/3.3.1/).
- **Seaborn (0.11.0)**: A Python visualization library based on Matplotlib for statistical graphics. [Seaborn Documentation](https://seaborn.pydata.org/).
- **Plotly (4.12.0)**: Python graphing library for interactive, publication-quality graphs. [Plotly Documentation](https://plotly.com/python/).
- **Streamlit (0.85.0)**: Facilitates the creation of data apps with minimal UI. [Streamlit Documentation](https://docs.streamlit.io/).
- **Kaggle**: For providing the dataset used in this project. [Kaggle Website](https://www.kaggle.com/).

## License

The project, originating from a private request, is released as open source. This decision is rooted in the philosophy that sharing such advancements benefits humanity. We believe in the transformative power of open-source collaboration.

## Conclusion

The project achieves a high level of accuracy in identifying powdery mildew in cherry leaves, confirming our hypothesis. However, it is limited by the need to use lower-resolution images (50x50 pixels) for manageability.

### Limitations

The project's current scope is limited to low-resolution, square-shaped images. Expanding to higher-resolution and varied aspect ratios could enhance the model's applicability.

### Future Development

Future development could focus on:

Adapting the model to handle higher-resolution images and different formats.
Creating algorithms to monitor agricultural areas or gardens, analyze photographs automatically, and trigger alarms if infections are detected.
