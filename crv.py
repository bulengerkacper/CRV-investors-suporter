import pandas_datareader.data as web
import matplotlib.pyplot as plt

import plotly.express as px
from datetime import date, datetime, timedelta
import datetime as dt

current_year=datetime.now().year
current_month=datetime.now().month
current_day=datetime.now().day

start_long_term = dt.datetime(2020, 8, 14) 
end_long_term = dt.datetime(current_year,current_month,current_day)

end_short_term_helper=datetime.now()-timedelta(3)
start_long_term = dt.datetime(2020, 1, 1)
end_short_term = dt.datetime(end_short_term_helper.year,end_short_term_helper.month,end_short_term_helper.day)

#data scraper
crv = web.DataReader("CRV-USD", 'yahoo', start_long_term, end_long_term)  # Collects data
crv.reset_index(inplace=True) 

##################
#print(crv)
#print (crv[-5:]) #LAST FIVE ELEMENTS

#########################
###SHORT ADVISOR
how_many_elements=5
sum=0
only_adj_close=crv["Adj Close"]
for rest in only_adj_close[-how_many_elements:]:
    print (rest)
    sum=sum+rest
sum=sum/how_many_elements
print("AVG:" + str(sum))
#####################

#######LONG_CHART##############
# crypto= crv[['Date','Adj Close']]
# crypto.set_index("Date", inplace=True)
# #FOR LONGERS
# fig = px.line(crypto, y=["Adj Close"] )
# fig.show();


