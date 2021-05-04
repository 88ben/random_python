# %%
from imdb import IMDb
from pprint import pprint

ia = IMDb()

movie = ia.get_movie('4154796')

pprint(sorted(movie.keys()))
print(movie['rating'])
print(movie['imdbID'])
print(movie['runtimes'][0])
print(movie['year'])
print(movie['genres'])
print(movie['votes'])


movies = ia.get_movie_list(['4154796','4154795'])
print(movies)