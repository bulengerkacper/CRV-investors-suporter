from flask import Flask
from crv import *
app = Flask(__name__)
scraper = Scrapper()

@app.route("/")
def hello_world():
    avg = scraper.short_advisor(10)
    return "<p>Hello, World!</p>"