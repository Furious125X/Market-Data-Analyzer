from analysis import load_prices, calculate_daily_returns

prices = load_prices("data/prices.csv")
daily_returns = calculate_daily_returns(prices)
print(f'Calculated {len(daily_returns)} daily returns.')
print(daily_returns[:5])  # Print the first 5 entries to verify
