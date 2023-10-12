'''
 This example will help you estimate potential losses in a portfolio over a specified time horizon for a given confidence level.
'''
import numpy as np

# Sample historical returns or price changes (replace with your own data)
returns = np.array([-0.02, 0.015, -0.03, 0.02, 0.01, -0.015, 0.025, -0.01, -0.015, 0.02])

# Confidence level (e.g., 95%)
confidence_level = 0.95

# Time horizon (e.g., 1 day)
time_horizon = 1

# Calculate VaR using historical simulation
sorted_returns = np.sort(returns)
var_index = int((1 - confidence_level) * len(returns))
var = -sorted_returns[var_index]

# Interpret the VaR result
print(f"VaR at {confidence_level * 100}% confidence over {time_horizon} day(s): {var * 100:.2f}%")

'''
Import the necessary libraries (NumPy).
Define a sample array of historical returns or price changes. You should replace this data with your own portfolio returns or price changes.
Set the confidence level (e.g., 95%) and time horizon (e.g., 1 day).
Calculate VaR using historical simulation. We sort the returns, find the index corresponding to the confidence level, and calculate the VaR as the negative of that return.
'''

'''
Result:: 
VaR at 95.0% confidence over 1 day(s): 3.00%

'''