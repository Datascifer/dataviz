import numpy as np
import pandas as pd

# Set a seed for reproducibility (optional)
np.random.seed(42)

# Define number of rows
num_rows = 100_000

# Generate synthetic data
customer_ids = np.arange(1, num_rows + 1)

# Income between 30,000 and 200,000
incomes = np.random.randint(30_000, 200_001, size=num_rows)

# Zipcodes (5-digit format from 10000 to 99999)
zipcodes = np.random.randint(10000, 99999, size=num_rows)

# Credit scores between 300 and 850
credit_scores = np.random.randint(300, 851, size=num_rows)

# Credit risk categories (Low, Medium, High)
credit_risk_categories = np.random.choice(["Low", "Medium", "High"], size=num_rows)

# Create the DataFrame
df_synthetic = pd.DataFrame({
    "customer_id": customer_ids,
    "income": incomes,
    "zipcode": zipcodes,
    "credit_score": credit_scores,
    "credit_risk": credit_risk_categories
})

# Display the first few rows
print(df_synthetic.head())

# Save to a CSV file
df_synthetic.to_csv("financial_data.csv", index=False)
