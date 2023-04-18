import pandas as pd
import yfinance as yf
from datetime import datetime
from datetime import timedelta
import plotly.graph_objects as go
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
import warnings
warnings.filterwarnings('ignore')
pd.options.display.float_format = '${:,.2f}'.format

#Getting the data:
today = datetime.today().strftime('%Y-%m-%d')
start_date = '2016-01-01'
eth_df = yf.download('ETH-USD',start_date, today) #download of ethereum data using yfinance

#check if we have null data on the df:
#print(eth_df.isnull().sum())
#see more about cleaning data: https://medium.com/bitgrit-data-science-publication/data-cleaning-with-python-f6bc3da64e45

#adjusting the column indexes (it lacks the 'date' index right now:
eth_df.reset_index(inplace=True) #not sure how this fixed the problem...
eth_df.columns

#Selecting the right columns (Prophet requires only two)
df = eth_df[["Date", "Open"]]

new_names = {
    "Date": "ds",
    "Open": "y",
}
df.rename(columns=new_names, inplace=True)

