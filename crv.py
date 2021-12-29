import pandas_datareader.data as web
import matplotlib.pyplot as plt

import plotly.express as px
from datetime import date, datetime, timedelta
import datetime as dt
import yfinance as yf


class Scrapper:
    def __init__(self):
        current_year=datetime.now().year
        current_month=datetime.now().month
        current_day=datetime.now().day
        start_long_term = dt.datetime(2020, 8, 14) 
        end_long_term = dt.datetime(current_year,current_month,current_day)
        end_short_term_helper=datetime.now()-timedelta(3)
        start_long_term = dt.datetime(2020, 1, 1)
        end_short_term = dt.datetime(end_short_term_helper.year,end_short_term_helper.month,end_short_term_helper.day)
        self.crv = web.DataReader("CRV-USD", 'yahoo', start_long_term, end_long_term)  # Collects data
        self.crv.reset_index(inplace=True)

    def avg_from_days(self,how_many_elements):
        sum=0
        only_adj_close=self.crv["Adj Close"]
        for rest in only_adj_close[-how_many_elements:]:
            sum=sum+rest
        sum=sum/how_many_elements
        return sum
    
    def reinitialize_dates(self):
        current_year=datetime.now().year
        current_month=datetime.now().month
        current_day=datetime.now().day

    def get_avg_from_last_15min(self):
        sum=0
        counter=0
        data = yf.download(tickers='CRV-USD', period = '15m', interval = '1m')
        for rest in data['Close']:
            sum=sum+rest
            counter+=1
        avg=sum/counter
        return avg


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