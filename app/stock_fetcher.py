import yfinance as yf

def get_stock_price(ticker):
    """Fetch latest stock price using Yahoo Finance."""
    try:
        stock = yf.Ticker(ticker)
        price = stock.history(period="1d")["Close"].iloc[-1]
        return round(price, 2)
    except Exception as e:
        return f"Error fetching stock price: {str(e)}"
