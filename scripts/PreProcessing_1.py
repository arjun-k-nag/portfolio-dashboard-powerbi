# -*- coding: utf-8 -*-
"""

@author: Arjun
"""
# Make sure to install yfinance library before running the script

# This script takes a csv file as input having two columns-|Company|Ticker| and generates a csv file having history data of closing price of all the Tickers present in the input csv file. 


import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

# Step 1: Load your tickers
companies = pd.read_csv("companies_with_tickers.csv")  # must have NSE_Ticker column

# Creating yfinance-compatible symbols (append .NS)
tickers = [ticker + ".NS" for ticker in companies["Ticker"].dropna().unique()]
print("Fetching data for:", tickers)

#################################
# Step 2: Define date range
#################################

years=5  # No of years data required

end_date = datetime.today().strftime("%Y-%m-%d")

start_date = (datetime.today() - timedelta(days=years*365)).strftime("%Y-%m-%d")


# Step 3: Downloading closing prices
data = yf.download(
    tickers,
    start=start_date,
    end=end_date,
    interval="1d",
    group_by="ticker",
    progress=True
)


# Step 4: Reformat into a clean DataFrame

closing_prices = pd.DataFrame()

for t in tickers:
    if t in data:  # ensures ticker exists in returned data
        temp = data[t][["Close"]].reset_index()
        temp["Ticker"] = t.replace(".NS", "")
        closing_prices = pd.concat([closing_prices, temp])

# Save to CSV
closing_prices.to_csv("nse_closing_prices.csv", index=False)

print("Saved data for", len(tickers), "companies into nse_closing_prices.csv")





