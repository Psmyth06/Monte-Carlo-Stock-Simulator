import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Monte Carlo Stock Simulator
# -----------------------------

# Model parameters
starting_price = 100
annual_return = 0.08
volatility = 0.20
trading_days = 252
num_simulations = 10000

dt = 1 / trading_days

# Store final prices from each simulation
final_prices = []

# Store a smaller number of full paths for plotting
sample_paths = []

# Run Monte Carlo simulations
for simulation in range(num_simulations):

    prices = [starting_price]

    for day in range(trading_days):
        random_shock = np.random.normal(0, 1)

        daily_return = (
            (annual_return - 0.5 * volatility**2) * dt
            + volatility * np.sqrt(dt) * random_shock
        )

        new_price = prices[-1] * np.exp(daily_return)
        prices.append(new_price)

    final_prices.append(prices[-1])

    # Save only the first 100 paths for plotting
    if simulation < 100:
        sample_paths.append(prices)


# -----------------------------
# Risk Analysis
# -----------------------------

final_prices = np.array(final_prices)

average_final_price = np.mean(final_prices)
median_final_price = np.median(final_prices)

probability_of_loss = np.mean(final_prices < starting_price)

percentile_5 = np.percentile(final_prices, 5)
percentile_95 = np.percentile(final_prices, 95)

value_at_risk_95 = starting_price - percentile_5


# -----------------------------
# Display Results
# -----------------------------

print("\nMonte Carlo Stock Price Simulation")
print("-----------------------------------")

print(f"Starting price: €{starting_price:.2f}")
print(f"Number of simulations: {num_simulations:,}")
print(f"Expected annual return: {annual_return:.2%}")
print(f"Annual volatility: {volatility:.2%}")

print("\nSimulation Results")
print("-----------------------------------")

print(f"Average final price: €{average_final_price:.2f}")
print(f"Median final price: €{median_final_price:.2f}")
print(f"Probability of loss: {probability_of_loss:.2%}")

print(f"5th percentile final price: €{percentile_5:.2f}")
print(f"95th percentile final price: €{percentile_95:.2f}")

print(f"95% Value at Risk: €{value_at_risk_95:.2f}")


# -----------------------------
# Plot Simulated Price Paths
# -----------------------------

plt.figure(figsize=(10, 6))

for path in sample_paths:
    plt.plot(path, alpha=0.2)

plt.axhline(
    starting_price,
    linestyle="--",
    label="Starting Price"
)

plt.title("Monte Carlo Stock Price Simulation")
plt.xlabel("Trading Day")
plt.ylabel("Stock Price (€)")
plt.legend()
plt.grid(True)

plt.show()


# -----------------------------
# Plot Final Price Distribution
# -----------------------------

plt.figure(figsize=(10, 6))

plt.hist(final_prices, bins=60)

plt.axvline(
    average_final_price,
    linestyle="--",
    label=f"Mean: €{average_final_price:.2f}"
)

plt.axvline(
    percentile_5,
    linestyle="--",
    label=f"5th Percentile: €{percentile_5:.2f}"
)

plt.title("Distribution of Simulated Final Stock Prices")
plt.xlabel("Final Stock Price (€)")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)

plt.show()
