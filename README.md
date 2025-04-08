# CALORIES BURNT PREDICTION USING XGBOOST

## OBJECTIVE

The goal of this project is to build a machine learning model that accurately predicts the number of calories burnt by a person based on various physiological and exercise-related parameters. This can help individuals monitor their fitness and make informed decisions about workouts, diet, and overall health. The project also includes a Streamlit-based web interface for easy interaction with the model.

---

## DATASET USED

The dataset used for this project is a combination of two CSV files:

- `calories.csv`
- `exercise.csv`

These were merged on the `User_ID` column, and irrelevant features like `User_ID` were dropped. After preprocessing, the final dataset includes the following columns:

### Dataset Columns and Descriptions

| Column        | Description                                                  |
|---------------|--------------------------------------------------------------|
| Gender        | Gender of the individual (`male` or `female`)                |
| Age           | Age of the person in years                                   |
| Height        | Height of the person in centimeters                          |
| Weight        | Weight in kilograms                                          |
| Duration      | Duration of the exercise session in minutes                  |
| Heart_Rate    | Heart rate during the exercise                               |
| Body_Temp     | Body temperature in Celsius                                  |
| Calories      | Target variable — calories burnt (used for prediction)       |

---

## HOW TO RUN THE APP

### 1. **Clone the Repository**

```bash
git clone https://github.com/FRO-54/Calories_prediction_ML
cd Calories_prediction_ML
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv env
```
Activate the Environment

Windows
```bash
env/Scripts/Activate
```

macOS/Linux
```bash
source env/bin/activate
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run src/App.py
```
This will launch the app in your browser. You can enter the required input values (Gender, Age, Weight, etc.), and the app will output the predicted calories burnt using the trained XGBoost model.
