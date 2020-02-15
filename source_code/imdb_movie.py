import pickle

def load_api_key():
    file = open('key.pkl', 'rb')
    key = pickle.load(file)
    print(key)

key = load_api_key()
