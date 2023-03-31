import pandas as pd

# load the data into dataframes
test_df = pd.read_csv('test_data.csv')
train_df = pd.read_csv('train_data.csv')
valid_df = pd.read_csv('valid_data.csv')
all_df = pd.read_csv('all_data.csv')

# remove rows with empty text in all data
all_df = all_df.dropna(subset=['review'])

# remove rows with duplicate text in all data
all_df = all_df.drop_duplicates(subset=['review'])

# remove rows with empty text in test data
test_df = test_df.dropna(subset=['text'])

# remove rows with duplicate text in test data
test_df = test_df.drop_duplicates(subset=['text'])

# remove rows with empty text in train data
train_df = train_df.dropna(subset=['text'])

# remove rows with duplicate text in train data
train_df = train_df.drop_duplicates(subset=['text'])

# remove rows with empty text in valid data
valid_df = valid_df.dropna(subset=['text'])

# remove rows with duplicate text in valid data
valid_df = valid_df.drop_duplicates(subset=['text'])

# save the cleaned data back to the csv files
test_df.to_csv('test_data_cleaned.csv', index=False)
train_df.to_csv('train_data_cleaned.csv', index=False)
valid_df.to_csv('valid_data_cleaned.csv', index=False)
all_df.to_csv('all_data_cleaned.csv', index=False)
