from flask import Flask, render_template
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
    avg = scraper.get_avg_from_last_15min()
    return str(avg)

@app.route("/compare_15min_to_3days")
def compare_15min_to_3days():
    return str(scraper.compare_15min_to_3days())