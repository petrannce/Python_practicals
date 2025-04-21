import yfinance as yf
import mplfinance as mpf
import pandas as pd

ticker = input("Enter the stock name: ")
df = yf.download(ticker, start="2023-01-01", end="2024-01-01")

# Print the column structure to understand what we're working with
print("Original columns structure:")
print(df.columns)

# Reset the index if it's a MultiIndex
if isinstance(df.columns, pd.MultiIndex):
    # Flatten multi-index columns
    df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]

# Another approach: create a new DataFrame with the required structure
new_df = pd.DataFrame()
new_df['Open'] = df['Open'].astype(float)
new_df['High'] = df['High'].astype(float)
new_df['Low'] = df['Low'].astype(float)
new_df['Close'] = df['Close'].astype(float)
new_df['Volume'] = df['Volume'].astype(int)
new_df.index = df.index

print("New DataFrame structure:")
print(new_df.head())
print(new_df.dtypes)

# Use the new DataFrame for plotting
mpf.plot(new_df, type='candle', style='charles',
         title=f'{ticker} Candlestick Chart', ylabel='Price', figsize=(10, 6),
         volume=True, show_nontrading=False)