import yfinance as yf
import datetime
from datetime import date, timedelta
today = date.today()

d1 = today.strftime('%Y-%m-%d')
end_date = d1
d2 = date.today()-timedelta(days=100)
d2 = d2.strftime('%Y-%m-%d')
start_date = d2
data = yf.download('GLAND.NS',
                   start=start_date,
                   end=end_date,
                   progress=False)

print(data)
# Stock Price
