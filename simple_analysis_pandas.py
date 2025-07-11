# Importing the required libraries
import pandas as pd
import numpy as np

# Loading a sample dataset (using a built-in dataset)
# You can replace this with any CSV file you have
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
data = pd.read_csv(url)

# Displaying the first few rows of the dataset
print("Dataset Head:")
print(data.head())

# Basic data info (e.g., number of entries, missing values)
print("\nData Info:")
print(data.info())

# Cleaning data (e.g., dropping rows with missing values)
data_cleaned = data.dropna()

# Summary statistics (mean, std, etc.)
print("\nSummary Statistics:")
print(data_cleaned.describe())

# Grouping the data by 'day' and calculating the average 'total_bill' and 'tip'
grouped_data = data_cleaned.groupby('day')[['total_bill', 'tip']].mean()
print("\nGrouped Data (Average Total Bill and Tip by Day):")
print(grouped_data)

# Creating a new column: tip percentage (tip/total_bill * 100)
data_cleaned['tip_percentage'] = (data_cleaned['tip'] / data_cleaned['total_bill']) * 100

# Display the new column
print("\nDataset with Tip Percentage Column:")
print(data_cleaned[['total_bill', 'tip', 'tip_percentage']].head())

# Visualization of 'total_bill' vs 'tip' (Optional, if you have matplotlib installed)
import matplotlib.pyplot as plt
data_cleaned.plot.scatter(x='total_bill', y='tip', color='blue', alpha=0.5)
plt.title('Total Bill vs Tip')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.show()
