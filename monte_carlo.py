# Monte Carlo Stock Price Simulator

starting_price = 100
annual_return = 0.08
volatility = 0.20
years = 1

print("Starting stock price:", starting_price)

import numpy as np

random_number = np.random.normal(0, 1)

print("Random shock:", random_number)

simulated_return = annual_return + volatility * random_number

future_price = starting_price * (1 + simulated_return)

print("Simulated return:", simulated_return)
print("Future stock price:", future_price)
