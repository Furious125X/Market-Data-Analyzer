from analysis import load_prices, calculate_daily_returns, calculate_moving_average, calculate_average_daily_return, calculate_volatility, best_and_worst_days, win_loss_analysis, plot_prices_with_moving_average, plot_daily_returns_histograms
import matplotlib.pyplot as plt

prices = load_prices("data/prices.csv")
daily_returns = calculate_daily_returns(prices)
average_daily_return = calculate_average_daily_return(daily_returns)
moving_averages = calculate_moving_average(prices, window_size=20)
volatility = calculate_volatility(daily_returns)
best_day, worst_day = best_and_worst_days(daily_returns)
win_loss = win_loss_analysis(prices, daily_returns)
win_loss = win_loss_analysis(prices, daily_returns)
print(f'Average Daily Return: {average_daily_return}')
print(f'Volatility: {volatility}')
print(f'Best Day: {best_day}')
print(f'Worst Day: {worst_day}')
print(f'Win/Loss Analysis: {win_loss}')
plot_prices_with_moving_average(prices, moving_averages)
plot_daily_returns_histograms(daily_returns)
