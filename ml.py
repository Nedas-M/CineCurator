import pandas as pd

pd.set_option('display.max_columns', None)
data = pd.read_csv('tmdb_5000_movies.csv')
print(data)