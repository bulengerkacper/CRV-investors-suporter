from flask import Flask, render_template, request
from crv import *
app = Flask(__name__)
# app.config["TEMPLATES_AUTO_RELOAD"] = True
scraper = Scrapper()

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/avg/<numb>")
def count_average(numb):
    avg = scraper.avg_from_days(int(numb))
    return str(avg)

@app.route("/avg_from_last_15min")
def get_avg_from_last_15min():
    return str(scraper.get_avg_from_last_15min())

@app.route("/compare_15min_to_days/<days>")
def compare_15min_to_x_days(days):
    return str(scraper.compare_15min_to_x_days(int(days)))

@app.route("/get_current_value")
def get_current_crypto():
    return str(scraper.get_current_crypto_value())

@app.route("/yesterday_to_today")
def yesterday_to_today():
    return scraper.yesterday_to_today()

@app.route("/coinswitcher", methods = ['POST'])
def coinswitcher():
    # data = request.form
    # print(request.form.get(['success_select']))
    json=request.get_json()
    # print(request.get_json())
    scraper.refresh_data(json['value'])
    # print(json['value'])
    return render_template("index.html")