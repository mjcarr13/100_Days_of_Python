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
    "function": "GLOBAL_QUOTE",
    "symbol": STOCK,
    "datatype": "json",
    "apikey": STOCKS_API_KEY,
}

news_parameters = {
    "apiKey": NEWS_API_KEY,
    "q": COMPANY_NAME,
    "searchIn": "title,description",
    "pageSize": "3"
}

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.

def stock_change_checker():
    response = requests.get(url=STOCK_ENDPOINT, params = stock_parameters)
    print(response.status_code)
    response.raise_for_status()
    stock_data = response.json()
    print(stock_data)
    global percentage_change
    percentage_change = float(stock_data["Global Quote"]["10. change percent"][:-1])
    if percentage_change >= 1 or percentage_change <= -1:
        print("Sending the news!")
        get_news()
    else:
        return False


def correct_arrow(change):
    if change >= 1:
        return f"🔺{round(change)}%"
    elif change <= -1:
        return f"🔻{round(change)}%"
    else:
        return None


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator

def get_news():
    response = requests.get(url=NEWS_ENDPOINT, params = news_parameters)
    print(response.status_code)
    response.raise_for_status()
    news_data = response.json()
    article_1_title = news_data["articles"][0]["title"]
    article_1_description = news_data["articles"][0]["description"]
    article_2_title = news_data["articles"][1]["title"]
    article_2_description = news_data["articles"][1]["description"]
    article_3_title = news_data["articles"][2]["title"]
    article_3_description = news_data["articles"][2]["description"]
    client = Client(account_sid,auth_token)
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body=f"{STOCK}: {correct_arrow(percentage_change)}\n"
             f"Headline: {article_1_title}\n"
             f"Brief: {article_1_description}\n"
             f"Headline: {article_2_title}\n"
             f"Brief: {article_2_description}\n"
             f"Headline: {article_3_title}\n"
             f"Brief: {article_3_description}\n",
        to="whatsapp:+447980086782"
    )


stock_change_checker()

