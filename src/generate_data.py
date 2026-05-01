import pandas as pd
import numpy as np

# Random dataset size
rows = 1000

# Generate synthetic data
data = {
    'tenure': np.random.randint(1, 72, rows),
    'MonthlyCharges': np.random.uniform(20, 120, rows),
    'TotalCharges': np.random.uniform(100, 8000, rows),
    'Churn': np.random.randint(0, 2, rows)
}

# Create dataframe
df = pd.DataFrame(data)

# Save CSV
df.to_csv('data/churn.csv', index=False)

print("Dataset Generated Successfully")