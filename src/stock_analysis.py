import yfinance as yf
import matplotlib.pyplot as plt

# Download data for one ticker
ticker = input('Enter a ticker symbol (e.g. AAPL): ')
data = yf.download(ticker, period='1y')

# Plot closing price
plt.figure(figsize=(10, 6))
plt.plot(data['Close'])
plt.title(f'{ticker} Closing Price (1Y)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.show()

# Basic statistics
stats = {
    'Mean': data['Close'].mean(),
    'Median': data['Close'].median(),
    'Standard Deviation': data['Close'].std(),
    'Minimum': data['Close'].min(),
    'Maximum': data['Close'].max()
}

print(f'\nBasic statistics for {ticker}:')
for k, v in stats.items():
    try:
    	print(f'{k}: {float(v):.2f}')
    except:
    	print(f'{k}: {v}')


# Compare multiple tickers
tickers = input('\nEnter tickers separated by commas (e.g. AAPL,MSFT,GOOG): ')
tickers = [t.strip() for t in tickers.split(',')]

multi_data = yf.download(tickers, period='1y')['Close']

plt.figure(figsize=(12, 7))
for t in tickers:
    plt.plot(multi_data.index, multi_data[t], label=t)
plt.title('Stock Closing Prices Comparison (1Y)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()
