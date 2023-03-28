import requests
from bs4 import BeautifulSoup
import csv

# URL of the top 250 movies page on IMDb
url = 'https://www.imdb.com/chart/top'

# Send a GET request to the URL and parse the HTML content using BeautifulSoup
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the movie titles and user review links on the page
titles = soup.find_all('td', class_='titleColumn')
links = soup.find_all('td', class_='titleColumn')

# Create a list to store the movie titles and user review links
movie_data = []

# Loop through each title and link and extract the text and URL values
for title, link in zip(titles, links):
    # Extract the movie title and release year
    movie_title = title.a.text
    release_year = title.span.text.strip('()')

    # Extract the user review link for the movie
    user_review_link = 'https://www.imdb.com' + link.a['href'] + 'reviews?ref_=tt_urv'

    # Add the movie title, release year, and user review link to the movie_data list
    movie_data.append([movie_title, release_year, user_review_link])

# Write the movie data to a CSV file
with open('top250_movie_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Movie Title', 'Release Year', 'User Review Link'])
    writer.writerows(movie_data)
