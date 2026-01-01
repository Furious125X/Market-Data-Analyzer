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

def calculate_average_daily_return(daily_returns):
    total_return = sum([ret["daily_return"] for ret in daily_returns])
    average_return = total_return / len(daily_returns) if daily_returns else 0
    return average_return

def calculate_moving_average(prices, window_size):
    moving_averages = []
    closes = [price["close"] for price in prices]
    
    for i in range(len(prices)):
        if i < window_size - 1:
            moving_averages.append({
                "date": prices[i]["date"],
                "moving_average": None
            })
        else:
            window = closes[i - window_size + 1:i + 1]
            moving_average = sum(window) / window_size
            moving_averages.append({
                "date": prices[i]["date"],
                "moving_average": moving_average
            })
    
    return moving_averages

def calculate_volatility(daily_returns):
    if not daily_returns:
        return 0
    
    mean_return = calculate_average_daily_return(daily_returns)
    squared_diffs = [(ret["daily_return"] - mean_return) ** 2 for ret in daily_returns]
    variance = sum(squared_diffs) / len(daily_returns)
    volatility = variance ** 0.5
    return volatility

def best_and_worst_days(daily_returns):
    if not daily_returns:
        return None, None
    
    best_day = max(daily_returns, key=lambda x: x["daily_return"])
    worst_day = min(daily_returns, key=lambda x: x["daily_return"])
    
    return best_day, worst_day

def win_loss_analysis(prices, daily_returns):
    if not prices or not daily_returns:
        return {"total_wins": 0, "total_losses": 0, "win_loss_ratio": None}
    
    total_wins = sum(1 for ret in daily_returns if ret["daily_return"] > 0)
    total_losses = sum(1 for ret in daily_returns if ret["daily_return"] < 0)
    win_loss_ratio = total_wins / total_losses if total_losses > 0 else None
    
    return {
        "total_wins": total_wins,
        "total_losses": total_losses,
        "win_loss_ratio": win_loss_ratio
    }

def plot_prices_with_moving_average(prices, moving_averages):
    import matplotlib.pyplot as plt

    dates = [price["date"] for price in prices]
    closes = [price["close"] for price in prices]
    ma_values = [ma["moving_average"] for ma in moving_averages]

    plt.figure(figsize=(12, 6))
    plt.plot(dates, closes, label='Closing Prices', color='blue')
    plt.plot(dates, ma_values, label='Moving Average', color='orange')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Prices with Moving Average')
    plt.legend()
    plt.savefig("price_&_ema.png")


def plot_daily_returns_histograms(daily_returns):
    import matplotlib.pyplot as plt

    returns = [ret["daily_return"] for ret in daily_returns]

    plt.figure(figsize=(10, 5))
    plt.hist(returns, bins=50, color='green', alpha=0.7)
    plt.xlabel('Daily Return')
    plt.ylabel('Frequency')
    plt.title('Histogram of Daily Returns')
    plt.savefig("daily_returns_histogram.png")


#Additional functions can be added here as needed


