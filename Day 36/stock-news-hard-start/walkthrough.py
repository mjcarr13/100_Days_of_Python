import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

percentage_change = 0

STOCK = "IBM"
COMPANY_NAME = "IBM"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCKS_API_KEY = os.getenv("STOCKS_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

#twilio account details
account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_TOKEN")

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCKS_API_KEY,
}

response = requests.get(url=STOCK_ENDPOINT, params = stock_parameters)
print(response.status_code)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in stock_data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
