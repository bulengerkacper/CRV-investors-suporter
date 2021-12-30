import re
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
        self.crv = web.DataReader("CRV-USD", 'yahoo', self.start_long_term, self.end_long_term)

    def avg_from_days(self,how_many_elements):
        sum=0
        only_adj_close=self.crv["Adj Close"]
        for rest in only_adj_close[-how_many_elements:]:
            sum=sum+rest
        return round(sum/how_many_elements,4)

    def get_avg_from_last_15min(self):
        sum=0
        how_many_elements=0
        data = yf.download(tickers='CRV-USD', period = '15m', interval = '1m')
        for rest in data['Close']:
            sum=sum+rest
            how_many_elements+=1
        return round(sum/how_many_elements,4)
    
    def get_current_value(self):
        data=yf.download(tickers='CRV-USD', period = '15m', interval = '1m')
        amount=data['Close']
        result=amount[-1:]
        return round(result.values[0],4)
    
    def compare_15min_to_x_days(self,days):
        from_last_15min=self.get_avg_from_last_15min()
        avg_from_days=self.avg_from_days(3)
        if (from_last_15min < days):
            return ("<span class='"'nes-text is-success'"'>Avg from last 15 min < " + str(days) + " days</span>")
        else:
            return ("<span class='"'nes-text is-error'"'>Avg from last 15 min > " +  str(days) + " days</span>")

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