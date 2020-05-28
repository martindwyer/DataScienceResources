import matplotlib.pyplot as plt
import pandas_datareader.data as pdr
import yfinance as yf
import pandas as pd
import seaborn as sns

#  Preparing the bank stock database using Yahoo Finance

yf.pdr_override()

sandp500 = pdr.get_data_yahoo("SPY", start="2016-04-30", end="2020-04-30")
bac = pdr.get_data_yahoo("BAC", start="2016-04-30", end="2020-04-30")
us_bank = pdr.get_data_yahoo("USB", start="2016-04-30", end="2020-04-30")
wells_fargo = pdr.get_data_yahoo("WF", start="2016-04-30", end="2020-04-30")
qcrh = pdr.get_data_yahoo("QCRH", start="2016-04-30", end="2020-04-30")
regions = pdr.get_data_yahoo("RF", start="2016-04-30", end="2020-04-30")
msft = pdr.get_data_yahoo("MSFT", start="2016-04-30", end="2020-04-30")
aapl = pdr.get_data_yahoo("AAPL", start="2016-04-30", end="2020-04-30")

tickers = ['SPY','BAC','USB','WF','QCRH','RF','MSFT','AAPL']

bank_stocks = pd.concat([sandp500, bac, us_bank, wells_fargo, qcrh, regions, msft, aapl], axis=1,keys = tickers)
bank_stocks.columns.names =['Bank Ticker','Stock Info']

bank_stocks.info()
print(bank_stocks.head())


# Creating a dataframe with bank daily returns

returns = pd.DataFrame()

for tick in tickers:
    returns[tick + ' Return'] = bank_stocks[tick]['Close'].pct_change()
    
returns.info()
print(returns.head())


# Exploring data about returns - correlations between bank stock returns

sns.pairplot(returns[1:],kind="reg")

# Print out a listing of the returns over the five years for each stock

total_returns = returns.cumsum()
print(total_returns.info())
print(total_returns.head())

print("\nFive year returns")
for tick in tickers:
    print("Total return for {} over the five-year period was equal to {}%".format(tick,total_returns['2020-04-27':'2020-04-27'][tick + ' Return']))
          

# Date of the biggest drop in return for each stock (All in March 2020)

print("\nThe day on which each stock had its biggest drop is as follows:")
print(returns.idxmin())

# Date of each stocks biggest return (within days of their big falls in March 2020)

print("\nThe day on which each stock had its biggest gain is as follows:")
print(returns.idxmax())


# Which stock has the highest risk based on variation in returns? (Regions RF)

print("\nThe follow is a list of standard deviation (risk) for each stock:")
print(returns.std())

# which stock has the highest market risk (beta)?

correlations = returns.corr()

market_risk = correlations['SPY Return']

print("\nThe follow list is each stock's correlation with market gains:")
print(market_risk)

sns.set_style('whitegrid')
for tick in tickers:
    bank_stocks[tick]['Close'].plot(figsize=(12,4),label=tick)
plt.legend()
plt.show()


"""

Come back for visualization after adept at plotly ... tutorial sessions ongoing.

"""








