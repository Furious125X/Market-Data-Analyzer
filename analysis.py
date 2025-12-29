import csv
from datetime import datetime

def load_prices(file_path):
    prices = []
    daily_prices = {}
    
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            close_time = datetime.strptime(row["Close time"], "%Y-%m-%d %H:%M:%S.%f")

            date = close_time.date() # Extract date part only
            daily_prices[date] = float(row["Close"])

    prices = [{"date": date, "close": close} for date, close in sorted(daily_prices.items())]
    return prices

def calculate_daily_returns(prices):
    daily_returns = []
    
    for i in range(1, len(prices)):
        previous_close = prices[i - 1]["close"]
        current_close = prices[i]["close"]
        daily_return = (current_close - previous_close) / previous_close
        daily_returns.append({
            "date": prices[i]["date"],
            "daily_return": daily_return
        })
    
    return daily_returns