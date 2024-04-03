from flask import Flask
 
app = Flask(__name__)

@app.route("/predict")
def predict():
    return "Hi"

if __name__ =='__main__':
    app.run(debug=True)