import numpy as np
import pandas as pd

# Set a seed for reproducibility (optional)
np.random.seed(42)

# Number of rows
num_rows = 10000

# Generate unique names for x
names = [f"Name_{i+1}" for i in range(num_rows)]

# Generate random bank balances for y (integers between 10 and 100,000)
balances = np.random.randint(10, 100001, size=num_rows)

# Possible music genres for z
genres = ["Rock", "Pop", "Jazz", "Classical", "Hip-Hop", "Electronic"]
favorite_genres = np.random.choice(genres, size=num_rows)

# Create the DataFrame
df = pd.DataFrame({
    "x": names,
    "y": balances,
    "z": favorite_genres
})

# Show the first few rows of the generated dataset
print(df.head())

# If desired, save to CSV
df.to_csv("sample_dataset.csv", index=False)
