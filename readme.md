This project is an AI powered Stock Market Agent that fetches real time stock prices and provides Buy/Sell/Hold recommendations based on the latest stock trends. The agent is built using Python,FastAPI,LangChain and Gemini API (Google AI). It is deployed on a public server (Render). The link for the deployed backend is here. https://stock-backend-7unk.onrender.com/

Since it is deployed on a free tier of render initial response for a get request can take up to 50 seconds after which responses come quickly when made.

This project fetches real time stock prices using Yahoo Finances' python module called yfinance and uses LangChain for intelligent response generation. It exposes a REST API that returns stock data and analysis, making it accessible for integration with other applications. A prompt is sent to provide Buy, Sell, or Hold recommendations from Google Gemini.


API Endpoints:

1. GET /api/stock/{ticker} - Fetch Stock Price & Recommendation
Description: Fetches the latest stock price for a given ticker symbol and provides a Buy/Sell/Hold recommendation.

Method: GET

Path Parameter:

ticker (string): The stock symbol (e.g., AAPL for Apple - https://stock-backend-7unk.onrender.com/stock/AAPL).


Example usage in postman with GET request:

https://stock-backend-7unk.onrender.com/stock/AAPL


