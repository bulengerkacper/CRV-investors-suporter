import pandas_datareader.data as web
import more_itertools
from datetime import date, datetime, timedelta
import yfinance as yf


class Scrapper:
    def __init__(self):
        self.coin_to_coin="CRV-USD"
        self.refresh_data(self.coin_to_coin)
    
    def refresh_data(self,coin_to_coin):
        self.coin_to_coin=coin_to_coin
        self.end_long_term = datetime(datetime.now().year,datetime.now().month,datetime.now().day)
        self.crv = web.DataReader(coin_to_coin, 'yahoo', datetime.now()-timedelta(180), self.end_long_term)
        self.only_adj_close=self.crv["Adj Close"]

    def avg_from_days(self,how_many_elements):
        self.refresh_data(self.coin_to_coin)
        sum=0
        for rest in self.only_adj_close[-how_many_elements:]:
            sum=sum+rest
        return round(sum/how_many_elements,4)

    def get_avg_from_last_15min(self):
        sum,how_many_elements = 0,0
        data = yf.download(tickers=self.coin_to_coin, period = '15m', interval = '1m')
        for rest in data['Close']:
            sum=sum+rest
            how_many_elements+=1
        return round(sum/how_many_elements,4)
    
    def get_current_crypto_value(self):
        data=yf.download(tickers=self.coin_to_coin, period = '1d', interval = '1m')
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
        prevday=self.only_adj_close[-1]
        curday=self.get_current_crypto_value()
        if(prevday>curday):
            result=(prevday-curday)/prevday*100
            return ("<span class='"'nes-text is-error'"'> -" + str(round(result,2)) + "</span>")
        elif(prevday<curday):
            result=(curday-prevday)/prevday*100
            round(result,2)
            return ("<span class='"'nes-text is-success'"'> +" + str(round(result,2)) + "</span>")
        elif(prevday==curday):
            return "Current day and previous are equal"

    def get_rsi(self,how_many_days): #tbi
        minus14days=self.end_long_term-timedelta(how_many_days)
        temp = web.DataReader(self.coin_to_coin, 'yahoo', minus14days, self.end_long_term)
        temp_only_adj_close=temp["Adj Close"]
        up_counter,down_counter,sum_up,sum_down=0,0,0,0
        for value,next_value in more_itertools.pairwise(temp_only_adj_close):
            if(next_value/value) > 1:
                sum_up=sum_up+value
                up_counter+=1
            else:
                sum_down=sum_down+value
                down_counter+=1
        avg_up=sum_up/up_counter
        avg_down=sum_down/down_counter
        rs=avg_up/avg_down
        rsi=100-100/(1+rs)
        return round(rsi,4)
        
    def fancy_loader(self):
        return "" #to be implemented
