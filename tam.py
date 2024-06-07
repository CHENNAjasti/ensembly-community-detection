import pandas as pd
import numpy as np

np.random.seed(2023)  # for reproducibility

# Read the CSV file into a pandas DataFrame (assuming 'your_file.txt' has the .csv extension)
df = pd.read_csv('ground_truth_community_membership.csv')

# Modify 260 random values in the 'cluster_id' column to random integers between 1 and 20 (inclusive)
df.loc[np.random.choice(df.index, size=260), 'cluster_id'] = np.random.randint(1, 21, size=260)

# Save the modified DataFrame back to a CSV file (assuming same filename with .csv extension)
df.to_csv('predicted_clusters.csv', index=False)  # Overwrites the original file

print("Successfully modified the CSV file!")
