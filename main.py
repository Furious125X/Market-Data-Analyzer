from analysis import load_prices

data = load_prices("data/prices.csv")

print(f'Loaded {len(data)} price points.')
print(data[:5])  # Print the first 5 entries to verify