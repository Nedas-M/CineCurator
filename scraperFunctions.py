# Functions to scrape top 10 movies in theatres and in current year

from bs4 import BeautifulSoup
import requests
import requests_cache
import logging

# Set up logging configuration to display debug messages
logging.basicConfig(level=logging.DEBUG)

# Define headers to mimic a web browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Install a cache for requests to avoid repeated network calls
requests_cache.install_cache('movieCache',expire_after = 3600)

# Function to fetch data from a given URL
def fetchData(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return BeautifulSoup(response.content, 'html.parser')
    else:
        print(f"Error: Couldn't fetch data. Status code: {response.status_code}")
        return None

# Function to extract movie data from the HTML elements
def extractData(movie_data):
    movies = []
    for movie in movie_data[:10]:
        title_element = movie.find('h3', attrs={'class': 'c-finderProductCard_titleHeading'})
        title = title_element.get_text(strip=True) if title_element else 'NO TITLE'

        desc_element = movie.find('div', attrs={'class': 'c-finderProductCard_description'})
        description = desc_element.get_text(strip=True) if desc_element else 'NO DESCRIPTION'

        score_element = movie.find('div', class_='c-siteReviewScore')
        score = score_element.get_text(strip=True) if score_element else 'NO SCORE'

        # Append the extracted data as a dictionary to the movies list
        movies.append({
            'title': title,
            'description': description,
            'score': score
        })

    return movies

# Function to print movie data in a formatted way
def printData(movies, header):
    print(f'\n////////////////////\n{header}\n////////////////////\n')
    for movie in movies:
        title = movie['title']
        description = movie['description']
        score = movie['score']
        print(f"{title}\n{description}\nScore: {score}\n")
