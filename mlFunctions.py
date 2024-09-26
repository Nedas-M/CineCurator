import ast

def extract_genre_names(genre_list):
    try:
        genre_list = ast.literal_eval(genre_list)
        return ', '.join([genre['name'] for genre in genre_list])
    except (ValueError, SyntaxError):
        return ''

def recommend(movie, newMovies, similarity):
    index = newMovies[newMovies['title'] == movie].index[0]
    print(f"Similarity scores for {movie}: {similarity[index]}")
    distance = sorted(
        list(enumerate(similarity[index])), 
        reverse=True, # if reverse=True it picks the lowest similarity score
        key=lambda vector: vector[1]
    )[:10]

    for i in distance:
        if newMovies.iloc[i[0]].title != movie:
            print(newMovies.iloc[i[0]].title)