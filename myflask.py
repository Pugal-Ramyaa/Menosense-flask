from flask import Flask, request, jsonify
from sklearn.preprocessing import LabelEncoder
import numpy as np
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained models
rf_best_model = joblib.load('C:/Users/Ramya/Desktop/New folder/tflite/rf_model.joblib')
gb_best_model = joblib.load('C:/Users/Ramya/Desktop/New folder/tflite/gb_model.joblib')
ada_best_model = joblib.load('C:/Users/Ramya/Desktop/New folder/tflite/ada_model.joblib')
xgb_best_model = joblib.load('C:/Users/Ramya/Desktop/New folder/tflite/xgb_model.joblib')
mlp_best_model = joblib.load('C:/Users/Ramya/Desktop/New folder/tflite/mlp_model.joblib')
extra_trees_best_model = joblib.load('C:/Users/Ramya/Desktop/New folder/tflite/et_model.joblib')
knn_best_model = joblib.load('C:/Users/Ramya/Desktop/New folder/tflite/knn_model.joblib')
svc_model = joblib.load('C:/Users/Ramya/Desktop/New folder/tflite/svc_model.joblib')
meta_model = joblib.load('C:/Users/Ramya/Desktop/New folder/tflite/meta_model.joblib')

# Load the recommendation models
recommendation_models = {}
for recommendation in ['lifestyle_modification', 't2dm', 'less_salt_intake', 'regular_exercise', 'nutrition_rich_food', 'medication']:
    model = joblib.load(f'C:/Users/Ramya/Desktop/New folder/tflite/{recommendation}_model.joblib')
    recommendation_models[recommendation] = model

# Define endpoint for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    user_input_encoded = {key: (1 if value == 'Yes' else 0 if value == 'No' else value) for key, value in data.items()}
    input_df = pd.DataFrame(user_input_encoded, index=[0])

    rf_pred_user = rf_best_model.predict([list(user_input_encoded.values())])
    gb_pred_user = gb_best_model.predict([list(user_input_encoded.values())])
    ada_pred_user = ada_best_model.predict([list(user_input_encoded.values())])
    xgb_pred_user = xgb_best_model.predict([list(user_input_encoded.values())])
    mlp_pred_user = mlp_best_model.predict([list(user_input_encoded.values())])
    extra_trees_pred_user = extra_trees_best_model.predict([list(user_input_encoded.values())])
    knn_pred_user = knn_best_model.predict([list(user_input_encoded.values())])
    svc_pred_user = svc_model.predict([list(user_input_encoded.values())])
    rf_pred_user = rf_best_model.predict([list(user_input_encoded.values())])
    gb_pred_user = gb_best_model.predict([list(user_input_encoded.values())])

    user_meta_input = np.column_stack((rf_pred_user, gb_pred_user, ada_pred_user, xgb_pred_user, mlp_pred_user, extra_trees_pred_user, knn_pred_user, svc_pred_user, rf_pred_user, gb_pred_user))
    user_pred_meta = meta_model.predict(user_meta_input)

    recommendations = [recommendation for recommendation, model in recommendation_models.items() if model.predict(input_df)[0] == 1]

    severity_mapping = {0: 'Mild', 1: 'Moderate', 2: 'Severe'}
    severity = severity_mapping[user_pred_meta[0]]
    print("hi")
    response = {
        'recommendations': recommendations,
        'severity': severity
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)