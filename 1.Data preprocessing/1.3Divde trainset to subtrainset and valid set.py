import pandas as pd
from sklearn.model_selection import train_test_split

# Load the train dataset into a pandas dataframe
train_df = pd.read_csv("train_data.csv")

# Split the data into child train and validation sets
train_data, valid_data = train_test_split(train_df, test_size=0.16, random_state=42)

# Save the child train and validation datasets to separate CSV files
train_data.to_csv("child_train_data.csv", index=False)
valid_data.to_csv("valid_data.csv", index=False)