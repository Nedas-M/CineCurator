# Functions to get genre names from column & finding top 10 most similar movies

import ast

# Function to extract genre names from a string representation of a list
def extract_genre_names(genre_list):
    try:
        genre_list = ast.literal_eval(genre_list) # Safely evaluate the string to a list
        return ', '.join([genre['name'] for genre in genre_list])
    except (ValueError, SyntaxError):
        return ''
# Function to recommend movies based on cosine similarity scores
def recommend(movie, newMovies, similarity):
    index = newMovies[newMovies['title'] == movie].index[0]
    print(f"Similarity scores for {movie}: {similarity[index]}")
    distance = sorted(
        list(enumerate(similarity[index])), 
        reverse=True,
        key=lambda vector: vector[1]
    )[:10]

    for i in distance:
        if newMovies.iloc[i[0]].title != movie:
            print(newMovies.iloc[i[0]].title)