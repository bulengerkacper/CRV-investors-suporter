import re
import pandas_datareader.data as web
import matplotlib.pyplot as plt

import plotly.express as px
from datetime import date, datetime, timedelta
import datetime as dt
import yfinance as yf


class Scrapper:
    def __init__(self):
        self.coin_to_coin="CRV-USD"
        self.refresh_data(self.coin_to_coin)
        #self.crv.reset_index(inplace=True)
    
    def refresh_data(self,coin_to_coin):
        self.current_year=datetime.now().year
        self.current_month=datetime.now().month
        self.current_day=datetime.now().day
        self.start_long_term = dt.datetime(2020, 8, 14) 
        self.end_long_term = dt.datetime(self.current_year,self.current_month,self.current_day)
        self.coin_to_coin=coin_to_coin
        self.crv = web.DataReader(coin_to_coin, 'yahoo', self.start_long_term, self.end_long_term)
        self.only_adj_close=self.crv["Adj Close"]

    def avg_from_days(self,how_many_elements):
        sum=0
        for rest in self.only_adj_close[-how_many_elements:]:
            sum=sum+rest
        return round(sum/how_many_elements,4)

    def get_avg_from_last_15min(self):
        sum=0
        how_many_elements=0
        data = yf.download(tickers=self.coin_to_coin, period = '15m', interval = '1m')
        for rest in data['Close']:
            sum=sum+rest
            how_many_elements+=1
        return round(sum/how_many_elements,4)
    
    def get_current_crypto_value(self):
        data=yf.download(tickers=self.coin_to_coin, period = '15m', interval = '1m')
        amount=data['Close']
        result=amount[-1:]
        return round(result.values[0],4)
    
    def compare_15min_to_x_days(self,days):
        from_last_15min=self.get_avg_from_last_15min()
        avg_from_days=self.avg_from_days(days)
        if(days<30): 
            red="<span class='"'nes-text is-error'"'>"
            green="<span class='"'nes-text is-success'"'>"
        else:#i will go to hell because of this part of code ^^
            red="<span class='"'nes-text is-success'"'>"
            green="<span class='"'nes-text is-error'"'>"
        end="</span>"
        if (from_last_15min < avg_from_days):
            return (green + "Avg from last 15 min < avg from " + str(days) + " days" + end)
        else:
            return (red + "Avg from last 15 min > avg from " + str(days) + " days" + end)
    
    def yesterday_to_today(self):
        prevday=self.only_adj_close[-2]
        curday=self.only_adj_close[-1]
        if(prevday>curday):
            result=(prevday-curday)/prevday*100
            return ("<span class='"'nes-text is-error'"'> -" + str(round(result,2)) + "</span>")
        elif(prevday<curday):
            result=(curday-prevday)/prevday*100
            round(result,2)
            return ("<span class='"'nes-text is-success'"'> +" + str(round(result,2)) + "</span>")
        elif(prevday==curday):
            return "Current day and previous are equal"



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