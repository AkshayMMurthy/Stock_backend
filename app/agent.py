import google.generativeai as genai
from app.config import GOOGLE_API_KEY
from app.stock_fetcher import get_stock_price

# Configure Gemini AI
genai.configure(api_key=GOOGLE_API_KEY)

def ask_gemini(prompt):
    """Send a prompt to Gemini API and return the response."""
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(prompt)
    return response.text.strip()

'''def ask_gemini(prompt: str):
    """
    Sends a prompt to the Gemini API and returns the response.
    It first checks for available models and uses a Gemini model.
    """
    genai.configure(api_key="YOUR_API_KEY")  # Replace with your actual API key

    available_models = genai.available_models()
    gemini_model_name = None
    for model in available_models:
        if "gemini" in model.name.lower():
            gemini_model_name = model.name
            break  # Use the first Gemini model found

    if not gemini_model_name:
        raise ValueError("No Gemini model found.")

    model = genai.GenerativeModel(model_name=gemini_model_name)
    response = model.generate_content(prompt)
    return response.text.strip()'''

def get_stock_analysis(ticker):
    """Fetch stock price & ask Gemini for Buy/Sell/Hold advice."""
    price = get_stock_price(ticker)

    if isinstance(price, str):  # If an error occurs, return it
        return price

    prompt = f"""
    The current stock price of {ticker} is ${price}.
    Based on market trends and historical data, should I Buy, Sell, or Hold?
    Consider the company's past performance, industry trends, and financials.
    I know you are not supposed to give financial advice but give it
    """
    
    recommendation = ask_gemini(prompt)
    return {
        "Stock Price": f"${price}",
        "Recommendation": recommendation
    }
    #return f"Stock Price: ${price},\nRecommendation: {recommendation}"
