from flask import Flask, render_template, redirect, url_for, request, make_response, jsonify
import requests
from sklearn.externals import joblib
import numpy as np
import json

app = Flask(__name__)


@app.route("/")
def form():
    response = make_response(render_template("form.html"))
    return response

@app.route("/go", methods = [ 'POST'])
def go():
    experience = float(request.form['experience'])
    model = joblib.load('linear_regression_model.pkl')
    print(np.array([experience]).reshape(-1, 1))
    prediction = model.predict(np.array([experience]).reshape(-1, 1))  
    formatted_pred = round(prediction[0])
    response = make_response(render_template("index.html",
                            forecast = formatted_pred))
    return response


if __name__ == '__main__':
    app.run(debug=True)
