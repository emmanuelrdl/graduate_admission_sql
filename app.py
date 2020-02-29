from flask import Flask, render_template, redirect, url_for, request, make_response, jsonify
import requests
import json

app = Flask(__name__)

dark_sky_api_key = "073ed950bcd367ad35e76ea60cf5511c"
ipstack_api_key ="55896dde6c19b26566166b446fe84094"

@app.route("/")
def form():
    response = make_response(render_template("form.html"))
    return response

@app.route("/weather", methods = [ 'POST'])
def weather():
    lat = request.form['latitude']
    long = request.form['longitude']
    dark_sky = requests.get("https://api.darksky.net/forecast/{}/{},{}".format(dark_sky_api_key,lat,long), params={"lang":"fr"}).json()
    response = make_response(render_template("index.html",
                            forecast = dark_sky))
    return response


if __name__ == '__main__':
    app.run(debug=True)
