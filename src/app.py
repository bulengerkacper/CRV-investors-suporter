from flask import Flask, render_template, request, redirect, url_for
from crv import *

app = Flask(__name__)
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
    scraper.refresh_data(scraper.coin_to_coin) # hate this. but it works
    return scraper.yesterday_to_today()

@app.route("/coinswitcher", methods = ['POST'])
def coinswitcher():
    if request.method == 'POST':
        json=request.get_json()
        scraper.refresh_data(json['value'])
        return redirect("127.0.0.1:5000")

@app.route("/rsi")
def rsi():
    return str(scraper.get_rsi())

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='127.0.0.1')