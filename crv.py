import pandas_datareader.data as web
import matplotlib.pyplot as plt

import plotly.express as px
from datetime import date, datetime, timedelta
import datetime as dt
import yfinance as yf


class Scrapper:
    def __init__(self):
        self.refresh_data()
        #self.crv.reset_index(inplace=True)
    
    def refresh_data(self):
        self.current_year=datetime.now().year
        self.current_month=datetime.now().month
        self.current_day=datetime.now().day
        self.start_long_term = dt.datetime(2020, 8, 14) 
        self.end_long_term = dt.datetime(self.current_year,self.current_month,self.current_day)
        self.crv = web.DataReader("CRV-USD", 'yahoo', self.start_long_term, self.end_long_term)  # Collects data

    def avg_from_days(self,how_many_elements):
        sum=0
        only_adj_close=self.crv["Adj Close"]
        for rest in only_adj_close[-how_many_elements:]:
            sum=sum+rest
        sum=sum/how_many_elements
        return sum

    def get_avg_from_last_15min(self):
        sum=0
        counter=0
        data = yf.download(tickers='CRV-USD', period = '15m', interval = '1m')
        for rest in data['Close']:
            sum=sum+rest
            counter+=1
        avg=sum/counter
        return avg
    
    def compare_15min_to_3days(self):
        from_last_15min=self.get_avg_from_last_15min()
        avg_from_3_days=self.avg_from_days(3)
        if (from_last_15min < avg_from_3_days):
            return "<span class='"'nes-text is-success'"'>Avg from last 15 min is < avg from 3 days</span>"
        else:
            return "<span class='"'nes-text is-error'"'>Avg from last 15 min is > avg from 3 days</span>"

    def compare_15min_to_5days(self):
        from_last_15min=self.get_avg_from_last_15min()
        avg_from_5_days=self.avg_from_days(5)
        if (from_last_15min < avg_from_5_days):
            return "<span class='"'nes-text is-success'"'>Avg from last 15 min is < avg from 5 days</span>"
        else:
            return "<span class='"'nes-text is-error'"'>Avg from last 15 min is > avg from 5 days</span>"

#data scraper
##################
#print(crv)
#print (crv[-5:]) #LAST FIVE ELEMENTS

#########################
###SHORT ADVISOR
#####################

#######LONG_CHART##############
# crypto= crv[['Date','Adj Close']]
# crypto.set_index("Date", inplace=True)
# #FOR LONGERS
# fig = px.line(crypto, y=["Adj Close"] )
# fig.show();