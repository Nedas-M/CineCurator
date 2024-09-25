import pandas as pd
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from mlFunctions import extract_genre_names, recommend

movies = pd.read_csv('tmdb_5000_movies.csv')

movies = movies[['id', 'title', 'overview', 'genres', 'vote_average']]

movies['genres'] = movies['genres'].apply(extract_genre_names)
movies['tags'] = movies['overview'] + movies['genres']
newMovies = movies.drop(columns=['overview', 'genres'])

countVector = CountVectorizer(max_features=4803, stop_words='english') 
vector = countVector.fit_transform(newMovies['tags'].values.astype('U')).toarray()  

similarity = cosine_similarity(vector)
recommend('The Shawshank Redemption', newMovies, similarity)