import ast

def extract_genre_names(genre_list):
    try:
        genre_list = ast.literal_eval(genre_list)
        return ', '.join([genre['name'] for genre in genre_list])
    except (ValueError, SyntaxError):
        return ''

def recommend(movie, newMovies, similarity):
    index = newMovies[newMovies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])[:10]
    for i in distance:
        print(newMovies.iloc[i[0]].title)