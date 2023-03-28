import pandas as pd

# load the data into dataframes
test_df = pd.read_csv('test_data.csv')
train_df = pd.read_csv('train_data.csv')
valid_df = pd.read_csv('valid_data.csv')

# remove rows with empty text
test_df = test_df.dropna(subset=['text'])
train_df = train_df.dropna(subset=['text'])
valid_df = valid_df.dropna(subset=['text'])

# remove rows with duplicate text
test_df = test_df.drop_duplicates(subset=['text'])
train_df = train_df.drop_duplicates(subset=['text'])
valid_df = valid_df.drop_duplicates(subset=['text'])

# save the cleaned data back to the csv files
test_df.to_csv('test_data_cleaned.csv', index=False)
train_df.to_csv('train_data_cleaned.csv', index=False)
valid_df.to_csv('valid_data_cleaned.csv', index=False)