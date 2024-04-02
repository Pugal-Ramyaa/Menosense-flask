from flask import Flask, request, jsonify
import numpy as np
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained models
#rf_best_model = joblib.load('./rf_model.joblib')
#gb_best_model = joblib.load('./gb_model.joblib')
#ada_best_model = joblib.load('./ada_model.joblib')
#xgb_best_model = joblib.load('./xgb_model.joblib')
#mlp_best_model = joblib.load('./mlp_model.joblib')
#extra_trees_best_model = joblib.load('./et_model.joblib')
#knn_best_model = joblib.load('./knn_model.joblib')
#svc_model = joblib.load('./svc_model.joblib')
#meta_model = joblib.load('./meta_model.joblib')

# Load the recommendation models
#recommendation_models = {}
#for recommendation in ['lifestyle_modification', 't2dm', 'less_salt_intake', 'regular_exercise', 'nutrition_rich_food', 'medication']:
#    model = joblib.load(f'./{recommendation}_model.joblib')
#   recommendation_models[recommendation] = model

# Define endpoint for making predictions
@app.route('/predict')
def predict():
    
    print("hi")

if __name__ == '__main__':
    app.run(debug=True)
