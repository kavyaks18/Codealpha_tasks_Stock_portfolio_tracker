# Stock Portfolio Tracker

A command-line application for managing a stock portfolio, built in Python. This application allows users to add or remove stocks, display the current portfolio, and update stock prices using the Alpha Vantage API.

## Features

- Add stocks to your portfolio with the number of shares.
- Remove stocks from your portfolio.
- Display the current state of your portfolio, including share quantities and prices.
- Update the stock prices in the portfolio based on real-time data from Alpha Vantage.
- Calculate and display the total value of the portfolio.

## Requirements

- Python 3.x
- The following Python libraries:
  - `requests`
  - `json` (part of the Python standard library)

You can install the required libraries using pip:

```bash
pip install requests
```

## Setup
- Clone this repository or download the script.
- Replace the API_KEY in the script with your own API key from Alpha Vantage. You can sign up for a free API key at Alpha Vantage.

**Follow the on-screen prompts to manage your stock portfolio. You can choose from the following options:**

- Add Stock: Enter the stock symbol and the number of shares to add.
- Remove Stock: Enter the stock symbol and the number of shares to remove.
- Display Portfolio: Show the current portfolio, including shares and prices.
- Update Stock Prices: Fetch the latest prices for stocks in the portfolio.
- Exit: Exit the program.


## Example Commands
- Add a stock: Choose option 1, then enter AAPL for Apple Inc. and 10 for the number of shares.
- Remove a stock: Choose option 2, then enter AAPL for Apple Inc. and 5 for the number of shares to remove.
- Display portfolio: Choose option 3 to see your current portfolio status.
- Update stock prices: Choose option 4 to refresh stock prices from the Alpha Vantage API.
