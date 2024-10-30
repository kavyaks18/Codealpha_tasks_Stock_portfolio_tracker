import requests
import json

API_KEY = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, shares):
        """Add a stock to the portfolio."""
        if symbol in self.portfolio:
            self.portfolio[symbol]['shares'] += shares
        else:
            self.portfolio[symbol] = {'shares': shares, 'price': 0.0}

    def remove_stock(self, symbol, shares):
        """Remove a stock from the portfolio."""
        if symbol in self.portfolio:
            if shares >= self.portfolio[symbol]['shares']:
                del self.portfolio[symbol]
            else:
                self.portfolio[symbol]['shares'] -= shares

    def get_stock_price(self, symbol):
        """Fetch the current stock price for a given symbol."""
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={API_KEY}'
        response = requests.get(url)
        data = response.json()

        try:
            latest_time = list(data['Time Series (1min)'].keys())[0]
            return float(data['Time Series (1min)'][latest_time]['1. open'])
        except KeyError:
            print(f"Error retrieving data for {symbol}: {data.get('Note', 'Invalid symbol or API limit reached')}")
            return None

    def update_portfolio_prices(self):
        """Update the portfolio with current stock prices."""
        for symbol in self.portfolio:
            price = self.get_stock_price(symbol)
            if price is not None:
                self.portfolio[symbol]['price'] = price

    def get_portfolio_value(self):
        """Calculate the total value of the portfolio."""
        total_value = 0.0
        for symbol, details in self.portfolio.items():
            total_value += details['shares'] * details['price']
        return total_value

    def display_portfolio(self):
        """Display the current state of the portfolio."""
        print("\nCurrent Stock Portfolio:")
        for symbol, details in self.portfolio.items():
            print(f"{symbol}: {details['shares']} shares @ ${details['price']:.2f} each")
        print(f"Total Portfolio Value: ${self.get_portfolio_value():.2f}")


def main():
    tracker = StockPortfolio()

    while True:
        print("\nOptions:")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Display Portfolio")
        print("4. Update Stock Prices")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            tracker.add_stock(symbol, shares)
            print(f"Added {shares} shares of {symbol}.")

        elif choice == '2':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares to remove: "))
            tracker.remove_stock(symbol, shares)
            print(f"Removed {shares} shares of {symbol}.")

        elif choice == '3':
            tracker.display_portfolio()

        elif choice == '4':
            tracker.update_portfolio_prices()
            print("Updated stock prices.")

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
