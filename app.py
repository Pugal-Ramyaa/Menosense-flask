from flask import Flask
 
app = Flask(__name__)

@app.route("/predict")
def predicr():
    return "Hi"

if __name__ =='__main__':
    app.run(debug=True)