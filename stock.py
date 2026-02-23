import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import pandas as pd
import seaborn as sb
import yfinance as yf  # Assuming yfinance for data API

sb.set_theme()

"""
STUDENT CHANGE LOG & AI DISCLOSURE:
----------------------------------
1. Did you use an LLM (ChatGPT/Claude/etc.)? Yes
2. If yes, what was your primary prompt? 
Used Claude Opus 4.6 as a learning aid to understand each method's purpose and implementation step by step.
----------------------------------
"""

DEFAULT_START = dt.date.isoformat(dt.date.today() - dt.timedelta(365))
DEFAULT_END = dt.date.isoformat(dt.date.today())


class Stock:
    def __init__(self, symbol, start=DEFAULT_START, end=DEFAULT_END):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.data = self.get_data()

    def get_data(self):
        """Downloads data from yfinance and triggers return calculation."""
        data = yf.download(self.symbol, start=self.start, end=self.end)
        data.index = pd.to_datetime(data.index)
        self.calc_returns(data)
        return data

    def calc_returns(self, df):
        """Adds 'Change', close to close and 'Instant_Return' columns to the dataframe."""
        df['Change'] = df['Close'].pct_change()
        df['Instant_Return'] = np.log(df['Close']).diff().round(4)

    def add_technical_indicators(self, windows=[20, 50]):
        """
        Add Simple Moving Averages (SMA) for the given windows
        to the internal DataFrame. Produce a plot showing the closing price and SMAs.
        """
        plt.figure(figsize=(12, 6))
        plt.plot(self.data.index, self.data['Close'], label='Close')

        for w in windows:
            col_name = f'SMA_{w}'
            self.data[col_name] = self.data['Close'].rolling(w).mean()
            plt.plot(self.data.index, self.data[col_name], label=col_name)

        plt.title(f'{self.symbol} Technical Indicators')
        plt.ylabel('Price')
        plt.xlabel('Date')
        plt.legend()
        plt.show()

    def plot_performance(self):
        """Plots cumulative growth of $1 investment."""
        first_close = self.data['Close'].iloc[0]
        performance = (self.data['Close'] / first_close - 1) * 100
        plt.figure(figsize=(12, 6))
        plt.plot(self.data.index, performance)
        plt.title(f'{self.symbol} Performance')
        plt.ylabel('% Gain/Loss')
        plt.xlabel('Date')
        plt.show()

    def plot_return_dist(self):
        """Plot a histogram of instantaneous returns."""
        plt.figure(figsize=(12, 6))
        sb.histplot(self.data['Instant_Return'].dropna(), kde=True)
        plt.title(f'{self.symbol} Return Distribution')
        plt.xlabel('Instant Return')
        plt.ylabel('Frequency')
        plt.show()


def main():
    novo_nordisk = Stock("NVO")
    print(novo_nordisk.data.head(10))
    novo_nordisk.plot_performance()
    novo_nordisk.plot_return_dist()
    novo_nordisk.add_technical_indicators()

if __name__ == "__main__":
    main()