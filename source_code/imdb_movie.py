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
# url pattern to get get movie info by its imdb id
url_movie = "http://www.omdbapi.com/?i={}&apikey=" + key

movie_title = input("Movie title to search: ")
try:
    resp = requests.get(url_movies_search.format(movie_title))
except:
    print('Something went wrong')
else:
    dic = resp.json()
    if dic['Response'] == 'True':
        movies_list = dic['Search']
        for movie_dict in movies_list:
            imdbID = movie_dict['imdbID']
            try:
                resp = requests.get(url_movie.format(imdbID))
            except:
                print('Something went wrong')
            else:
                movie_dict = resp.json()
                title = movie_dict['Title']
                year = movie_dict['Year']
                movie_type = movie_dict['Type']
                poster_url = movie_dict['Poster']
                synopsis = movie_dict['Plot']
                print(f'\n{title} - {year} - {movie_type} - {imdbID} - {poster_url} - {synopsis}')
    else:
        print('No movie found with this title')
