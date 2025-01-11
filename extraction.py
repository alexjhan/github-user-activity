import requests

input_username = input("Enter your username: ")
url_events='https://api.github.com/users/'+input_username+'/events' # URL to get the user's events
url_red='https://api.github.com/users/'+input_username+'/repos' # URL to get the user's repos
url_blue='https://api.github.com/users/'+input_username # URL to get the user's profile
url_followers='https://api.github.com/users/'+input_username+'/followers' # URL to get the user's followers

def extract_events():
    response = requests.get(url_events).json()
    print(response)
def extract_red():
    response = requests.get(url_red)
    print(response.json())
def extract_blue():
    response = requests.get(url_blue)
    print(response.json())
def extract_followers():    
    response = requests.get(url_followers)
    print(response.json())
