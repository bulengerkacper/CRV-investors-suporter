from flask import Flask, render_template
from crv import *
app = Flask(__name__)
scraper = Scrapper()

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/avg/<numb>")
def count_average(numb):
    avg = scraper.short_advisor(int(numb))
    return str(avg)