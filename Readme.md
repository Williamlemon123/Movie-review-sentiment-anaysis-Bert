#1.Data processing
##1.1 Movie review url
This step is a Python script that uses external libraries to scrape the top 250 movies page on IMDb, extract movie data, and write it to a CSV file. The requests library is used to send a GET request to the page and retrieve the HTML content, which is then parsed using the BeautifulSoup library. The script extracts the movie titles, release years, and user review links using the find_all method and st
ores them in a list. A loop is used to iterate over the extracted data and add it to the list. Finally, the script uses the csv library to write the extracted data to a CSV file. Overall, this script demonstrates how to use Python and external libraries to extract and store data from web pages.

##1.2 Crawl reviews and divide to train and test set
The step is a Python script that uses various external libraries and tools to scrape user reviews from IMDb for the top 250 movies and perform sentiment analysis. The script starts by importing the required libraries, including numpy, pandas, scrapy, selenium, and tqdm. It also initializes a webdriver object using ChromeDriver.

Next, the script reads in movie data from a CSV file containing movie titles and review URLs. It then loops over each movie, scrapes user reviews for the movie, and stores the review text, sentiment (positive/negative), and label (1/0) in separate lists. The script uses selenium and scrapy libraries to scrape and parse review data, respectively.

Once all reviews have been scraped and sentiment labels assigned, the script combines the review, sentiment, and label lists into a pandas dataframe. It then shuffles the data and splits it into training and testing sets, with an 80/20 split. Finally, the script writes the training and testing dataframes to CSV files and closes the webdriver.

Overall, this script demonstrates how to use Python and external libraries to perform web scraping and sentiment analysis. It also showcases the use of ChromeDriver and selenium for automated browsing and web scraping.

##1.3 Divde trainset to subtrainset and valid set.

In this step, the pandas library is used to load a CSV file containing training data into a dataframe. Then, the train_test_split function from the sklearn.model_selection module is used to split the data into two sets: a child train set and a validation set. The split is done randomly, with 20% of the data assigned to the validation set and a random state of 42 is set to ensure the same split can be reproduced. Finally, the two resulting dataframes are saved as separate CSV files. Overall, this code uses machine learning technologies, specifically the train_test_split function from the scikit-learn library, to split a dataset into training and validation sets for use in a machine learning model.

##1.4 Data cleaning
This step is used to clean and preprocess data for a machine learning task. The data is loaded from csv files into pandas dataframes. The dataframes are then cleaned by removing rows with empty text and duplicate text. The cleaned data is then saved back into csv files with a suffix "_cleaned" added to their names. The technology used in this code is Python, specifically the pandas library, which is a powerful library for data manipulation and analysis. This code also utilizes common data cleaning techniques such as removing duplicates and null values from the data.

#2.DATA VISUALIZATION
Loading data from a CSV file using the pandas library.
Checking the shape and size of the dataset using pandas.
Exploring the data using head() function to get a glimpse of the first few rows of the data.
Encoding categorical variables using a dictionary and applying the encoding using the apply() function in pandas.
Conducting exploratory data analysis (EDA) using various data visualization techniques such as bar plots, box plots, and histograms using seaborn and matplotlib libraries.
Using the wordcloud library to create word clouds for visualizing the most frequent words used in the positive and negative reviews.

#3.Built BERT Model and comparison
##3.1 Loading the pre-trained BERT model and preprocessor
The code starts by loading the pre-trained BERT model from TensorFlow Hub as an encoder, which is designed to convert text into dense vectors. The specific BERT model used here is 'small_bert/bert_en_uncased_L-4_H-512_A-8'. This is a smaller BERT model with four layers, 512 hidden units, and 8 attention heads. The preprocessor model 'bert_en_uncased_preprocess/3' is also loaded, which is used to preprocess the text input. The preprocessor takes care of tokenization, padding, and other preprocessing steps required for BERT model input.

##3.2 Defining the fine-tuned model
After loading the pre-trained BERT model and preprocessor, a simple fine-tuned model is defined. The model includes the preprocessor, the BERT encoder, a dense layer with sigmoid activation, and a dropout layer. The dense layer is used to classify the text input into two categories: "toxic" or "non-toxic". The dropout layer is added to prevent overfitting.

##3.3 Compiling the model
The model is compiled with the BinaryCrossentropy loss function, which is commonly used for binary classification problems, and the AdamW optimizer, which is an extension of the Adam optimizer that is better suited for training deep learning models.

##3.4 Training the model
The model is trained on the training data for a specified number of epochs. In this case, the model is trained for 10 epochs. The number of epochs is a hyperparameter that determines how many times the model will see the training data during training.

##3.5 Evaluating the model
After training, the model is evaluated on both the validation and test datasets. The validation set is used to monitor the performance of the model during training, while the test set is used to evaluate the final performance of the model. The evaluation metric used here is accuracy, which is the proportion of correctly classified examples out of all examples.

##3.6 Results
The final accuracy on the test set is reported as 0.9075, which means that the model correctly classified 90.75% of the examples in the test set. This is a very good result, and it suggests that the model is effective at classifying toxic comments.

##3.7 Fine-tuning and warmup
The code also includes fine-tuning and warmup steps, which are used to adapt the pre-trained BERT model to the specific task of classifying toxic comments. Fine-tuning involves adjusting the weights of the pre-trained model based on the task-specific training data, while warmup involves gradually increasing the learning rate during the early stages of training to help the model converge faster. These steps are critical for achieving good performance on the task.
