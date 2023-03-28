import numpy as np
import pandas as pd
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from tqdm import tqdm
import warnings
import random

warnings.filterwarnings("ignore")

# Initialize webdriver
driver = webdriver.Chrome('chromedriver.exe')

# Load movie data
top250_movie_data = pd.read_csv('top250_movie_data.csv')

# Initialize lists to store review data
rating_list = []
review_list = []
label_list = []

# Loop over each movie and scrape reviews
for index, row in top250_movie_data.iterrows():
    movie_title = row['Movie_Title'] # set movie_title before scraping reviews for each movie
    try:
        movie_url = row['Review_URL'] + 'reviews?ref_=tt_urv'
        driver.get(movie_url)
        time.sleep(3)

        body = driver.find_element(By.CSS_SELECTOR, 'body')
        for i in range(3):
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(2)

        sel = Selector(text=driver.page_source)
        review_counts = sel.css('.lister .header span::text').extract_first().replace(',', '').split(' ')[0]
        more_review_pages = int(int(review_counts) / 25)

        for i in tqdm(range(more_review_pages)):
            try:
                css_selector = 'load-more-trigger'
                driver.find_element(By.ID, css_selector).click()
                time.sleep(3)
            except:
                pass

        reviews = driver.find_elements(By.CSS_SELECTOR, 'div.review-container')
        for d in tqdm(reviews):
            try:
                sel2 = Selector(text=d.get_attribute('innerHTML'))
                rating = sel2.css('.rating-other-user-rating span::text').extract_first()
                if rating is not None:
                    rating = int(rating)
                    if rating >= 7:
                        sentiment = 'positive'
                        label = 1
                    elif rating <= 6:
                        sentiment = 'negative'
                        label = 0
                    review = sel2.css('.text.show-more__control::text').extract_first()
                    if review is not None:
                        rating_list.append(sentiment)
                        review_list.append(review)
                        label_list.append(label)
            except:
                pass

    except:
        pass

# Combine review, rating and label lists into dataframe
data = pd.DataFrame({'Review': review_list, 'Sentiment': rating_list, 'Label': label_list})

# Shuffle data and split into training and testing sets
data = data.sample(frac=1, random_state=42)
train_size = int(len(data) * 0.8)
train_data = data[:train_size]
test_data = data[train_size:]

# Write dataframes to CSV files
train_data.to_csv('train_data.csv', index=False)
test_data.to_csv('test_data.csv', index=False)

# Close the webdriver
driver.quit()
