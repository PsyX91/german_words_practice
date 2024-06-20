from flask import Flask, request, render_template, jsonify
import pandas as pd
from grade_master_ai.models.model import from_df

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    student_info = {
        "maths_module_1": [data["maths_module_1"]],
        "maths_module_2": [data["maths_module_2"]],
        "maths_module_3": [data["maths_module_3"]],
        "english_module_1": [data["english_module_1"]],
        "english_module_2": [data["english_module_2"]],
        "english_module_3": [data["english_module_3"]],
        "science_module_1": [data["science_module_1"]],
        "science_module_2": [data["science_module_2"]],
        "science_module_3": [data["science_module_3"]],
        "science_module_4": [data["science_module_4"]],
        "attendance": [data["attendance"]],
        "study_hours": [data["study_hours"]],
    }

    df_new_student = pd.DataFrame(student_info)
    df = pd.read_csv("data/model_input.csv")

    # Use the model to predict
    predicted_grade, mae, r2 = from_df("linear_regression", df, df_new_student)

    result = {"predicted_grade": predicted_grade, "mae": mae, "r2": r2}

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
