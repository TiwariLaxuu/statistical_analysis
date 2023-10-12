'''
This example will help you determine whether a time series is stationary or non-stationary.
'''

import pandas as pd
import numpy as np
import statsmodels.api as sm

# Sample time series data (replace with your own data)
data = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# Create a pandas Series
time_series = pd.Series(data)

# ADF test
adf_test = sm.tsa.adfuller(time_series)

# Extract ADF test results
adf_statistic, p_value, lags, nobs, critical_values, icbest = adf_test

# Print the results
print(f'ADF Statistic: {adf_statistic}')
print(f'p-value: {p_value}')
print(f'Number of Lags: {lags}')
print(f'Number of Observations: {nobs}')
print('Critical Values:')
for key, value in critical_values.items():
    print(f'   {key}: {value}')
    
# Interpret the results
if p_value < 0.05:
    print("Reject the null hypothesis. The data is stationary.")
else:
    print("Fail to reject the null hypothesis. The data is non-stationary.")


'''
Import the necessary libraries, including pandas for handling time series data and statsmodels for the ADF test.
Create a sample time series using a list of data points. Replace this with your own time series data.
Use sm.tsa.adfuller to perform the ADF test on the time series.
Extract and print the ADF statistic, p-value, number of lags used, number of observations, and critical values.
Interpret the results based on the p-value. If the p-value is less than 0.05 (you can adjust the significance level), we reject the null hypothesis and conclude that the data is stationary; otherwise, we consider it non-stationary.

'''

'''
Result::
ADF Statistic: -0.3988620176087322
p-value: 0.910288606359724
Number of Lags: 2
Number of Observations: 7
Critical Values:
   1%: -4.9386902332361515
   5%: -3.477582857142857
   10%: -2.8438679591836733
Fail to reject the null hypothesis. The data is non-stationary.


'''