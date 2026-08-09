# Monte Carlo Stock Price Simulator

starting_price = 100
annual_return = 0.08
volatility = 0.20
years = 1

print("Starting stock price:", starting_price)

import numpy as np

random_number = np.random.normal(0, 1)

print("Random shock:", random_number)
