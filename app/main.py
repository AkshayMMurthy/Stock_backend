from fastapi import FastAPI
from agent import get_stock_analysis

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Stock Market AI Agent is Running!"}

@app.get("/stock/{ticker}")
def stock_price(ticker: str):
    """Fetch stock price & AI analysis for a given ticker."""
    result = get_stock_analysis(ticker)
    return {"response": result}

# Run server: uvicorn main:app --reload
