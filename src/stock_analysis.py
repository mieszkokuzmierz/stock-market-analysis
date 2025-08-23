import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Choose the stock ticker - let's start with checking Apple's prices
ticker = 'AAPL'

# Download last 1 year of data
data = yf.download(ticker, period='1y')

# Display first 5 rows
print('Data for stock:', ticker)
print(data.head())

# Plot closing price
plt.figure(figsize=(10, 5))
plt.plot(data.index, data['Close'], label='Close Price')
plt.title(f'{ticker} - Closing Price (Last 1 Year)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid()
plt.show()
