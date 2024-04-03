from flask import Flask
import numpy as np
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained models
rf_best_model = joblib.load('./rf_model.joblib')
gb_best_model = joblib.load('./gb_model.joblib')
ada_best_model = joblib.load('./ada_model.joblib')
xgb_best_model = joblib.load('./xgb_model.joblib')
mlp_best_model = joblib.load('./mlp_model.joblib')
extra_trees_best_model = joblib.load('./et_model.joblib')
knn_best_model = joblib.load('./knn_model.joblib')
svc_model = joblib.load('./svc_model.joblib')
meta_model = joblib.load('./meta_model.joblib')

@app.route("/predict")
def predict():
    return "Hi"

if __name__ =='__main__':
    app.run(debug=True)