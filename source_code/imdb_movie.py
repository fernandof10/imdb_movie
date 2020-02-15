import pickle
import requests


def load_api_key():
    """Return the API string stored in key.pkl."""
    file = open('key.pkl', 'rb')
    key = pickle.load(file)
    return key


# omdbapi API key
key = load_api_key()
# url pattern to search movies by title
url_movies_search = "http://www.omdbapi.com/?s=\"{}\"&apikey=" + key

movie_title = input("Movie title to search: ")
try:
    resp = requests.get(url_movies_search.format(movie_title))
except:
    print('Something went wrong')
else:
    movies_list = resp.json()['Search']
    for movie_dict in movies_list:
        title = movie_dict['Title']
        year = movie_dict['Year']
        imdbID = movie_dict['imdbID']
        movie_type = movie_dict['Type']
        poster_url = movie_dict['Poster']
        print(f'{title} - {year} - {movie_type} - {imdbID} - {poster_url}')
