# %%
from omdbapi.movie_search import GetMovie
from keys import OMDB_API_KEY

movie = GetMovie(title="Interstellar", api_key=OMDB_API_KEY)
# movie.get_all_data().keys()
# movie.get_data('Title', 'Year', 'Rated', 'Released', 'Runtime', 'Genre', 'Director', 'Writer', 'Actors', 'Plot', 'Poster', 'Ratings', 'Metascore', 'imdbRating', 'imdbVotes', 'imdbID', 'Type')

title, year, rated = movie.get_data('Title', 'Year', 'Rated').values()

print(title, year, rated)
