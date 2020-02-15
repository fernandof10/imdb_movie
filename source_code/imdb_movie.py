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


def get_movie_info(imdbID):
    """This function prints the movie details specified by imdbID argument."""
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

def new_search():
    movie_title = input("Movie title to search: ")
    try:
        resp = requests.get(url_movies_search.format(movie_title))
    except:
        print('Something went wrong')
    else:
        dic = resp.json()
        if dic['Response'] == 'True':
            movies_list = dic['Search']
            current_movie_index = 0
            while current_movie_index != 'exit':
                movie = movies_list[current_movie_index]
                imdbID = movie['imdbID']
                get_movie_info(imdbID)
                previous_next_movie = input('Choose next or prev: ')
                if previous_next_movie == 'next':  # goes to the next movie
                    current_movie_index += 1
                    if current_movie_index >= len(movies_list):  # goes to the list begginig
                        current_movie_index = 0
                elif previous_next_movie == 'prev':  # goes to the previous movie
                    current_movie_index -= 1
                    if current_movie_index < 0:  # goes to the end of the list
                        current_movie_index = len(movies_list) - 1
                else:
                    print('Exiting...')
                    current_movie_index = 'exit'
        else:
            print('No movie found with this title')


search = 'yes'
while search == 'yes':
    new_search()
    search = input('Do you want to do a new search(yes/not)? ')
