import smtplib

import requests
import day32.config as mail_config
import day36.config as config
from datetime import datetime, timedelta

today = datetime. today()
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_api_parameters={
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "datatype": "json",
    "apikey": config.STOCK_API_KEY
}

news_api_parameters={
    "apiKey": config.NEWS_API_KEY,
    "q": COMPANY_NAME,
    "language": "en"
}

stock_data = requests.get(url=STOCK_ENDPOINT, params=stock_api_parameters)
stock_data.raise_for_status()

one_day_before = (today - timedelta(days=1)).date()
two_days_before = (today - timedelta(days=2)).date()
price_yesterday = float(stock_data.json()["Time Series (Daily)"][str(two_days_before)]["4. close"])
price_day_before_yesterday = float(stock_data.json()["Time Series (Daily)"][str(one_day_before)]["4. close"])

difference = price_yesterday - price_day_before_yesterday
percent_difference = difference/price_yesterday*100

if abs(percent_difference) >= 5:
    if percent_difference > 0:
        symbol = "+"
    else:
        symbol = "-"
    news_data = requests.get(url=NEWS_ENDPOINT, params=news_api_parameters)
    news_data.raise_for_status()
    news_items = news_data.json()["articles"][0:3]
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=mail_config.gmail_user, password=mail_config.gmail_special_pass)
        for news in news_items:
            title = news['title']
            subject = f"TSLA: {symbol}-{abs(round(percent_difference))}% Headline: {title}".encode("ascii", "ignore")
            description = str(news["description"])
            description = description.encode("ascii", "ignore")

            connection.sendmail(from_addr=mail_config.gmail_user,
                                to_addrs=mail_config.yahoo_user,
                                msg=f"Subject:{subject}\n\n{description}")








## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

