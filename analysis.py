import csv
from datetime import datetime

def load_prices(file_path):
    prices = []
    
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            prices.append({
                "date": datetime.strptime(row["Close time"], "%Y-%m-%d %H:%M:%S.%f"),
                           "close" : float(row["Close"])})
    return prices