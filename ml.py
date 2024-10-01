# Reading data, vectorising data, using cosine similarity

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from mlFunctions import extract_genre_names, recommend

# Load movie data from a CSV file into a DataFrame
movies = pd.read_csv('tmdb_5000_movies.csv')

movieinp = input('Movie: ')

# Select relevant columns from the DataFrame
movies = movies[['id', 'title', 'overview', 'genres', 'vote_average']]

movies['genres'] = movies['genres'].apply(extract_genre_names)
movies['tags'] = movies['overview'] + movies['genres']
newMovies = movies.drop(columns=['overview', 'genres'])

# Initialize a CountVectorizer to convert text data into a matrix of token counts
countVector = CountVectorizer(max_features=4803, stop_words='english') 
vector = countVector.fit_transform(newMovies['tags'].values.astype('U')).toarray() # Fit and transform the tags

similarity = cosine_similarity(vector)

recommend(movieinp, newMovies, similarity)