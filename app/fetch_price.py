import yfinance as yf

def get_stock_price(ticker):
    """
    Fetches the latest stock price for a given ticker.
    """
    try:
        stock = yf.Ticker(ticker)
        price = stock.history(period="1d")["Close"].iloc[-1]  # Get latest closing price
        return round(price, 2)  # Return price rounded to 2 decimal places
    except Exception as e:
        return f"Error fetching stock price: {str(e)}"
