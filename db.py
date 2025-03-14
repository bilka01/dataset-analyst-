import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
# Replace 'your_dataset.csv' with your actual dataset file
df = pd.read_csv('your_dataset.csv')

# Display the first few rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())

# Display basic statistical analysis
print("\nBasic Statistical Analysis:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Generate a simple plot (e.g., histogram of a specific column)
# Replace 'column_name' with the actual column you want to plot
df['column_name'].hist(bins=20)
plt.title('Histogram of column_name')
plt.xlabel('column_name')
plt.ylabel('Frequency')
plt.show()