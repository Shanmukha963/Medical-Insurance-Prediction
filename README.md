# Insurance Cost Prediction with Streamlit

This project provides an interactive web application built with Streamlit to predict insurance costs based on various personal factors.

## Features
- Predict insurance charges based on age, sex, BMI, number of children, smoking status, and region.
- User-friendly interface for inputting details.
- Built using a Random Forest Regressor model.

## Getting Started

### Prerequisites
- Python 3.x
- Git (for cloning the repository)

### Installation

1.  **Clone the repository (if applicable):**
    ```bash
    git clone <your-github-repo-url>
    cd <your-repo-name>
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Streamlit Application

1.  **Ensure you have `app.py` and `insurance_model.pkl` in the same directory.**

2.  **Run the application:**
    ```bash
    streamlit run app.py
    ```

    This will open the application in your web browser.

## Project Structure
- `app.py`: The main Streamlit application script.
- `insurance_model.pkl`: The pre-trained machine learning model for predictions.
- `requirements.txt`: Lists all Python dependencies.
- `README.md`: Project documentation.

## Model Details
The prediction model is a Random Forest Regressor trained on the medical insurance dataset. It takes the following features as input:
- `age`: Age of the primary beneficiary.
- `sex`: Gender of the primary beneficiary.
- `bmi`: Body Mass Index.
- `children`: Number of children covered by health insurance.
- `smoker`: Smoking status.
- `region`: Residential area in the US (northeast, southeast, southwest, northwest).

## Deployment on Streamlit Community Cloud (Optional)

1.  **Push your code to a GitHub repository.** Ensure `app.py`, `insurance_model.pkl`, and `requirements.txt` are in the root directory.
2.  **Go to [Streamlit Community Cloud](https://share.streamlit.io/).**
3.  **Click 'New app' and connect your GitHub repository.**
4.  **Select the branch and the main file (`app.py`).**
5.  **Click 'Deploy!'**

Your application will be live in a few minutes!

## License

This project is open-source and available under the [MIT License](LICENSE).

from google.colab import files
files.download("README.md")
