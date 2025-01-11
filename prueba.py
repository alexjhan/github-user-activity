import requests

input_username = input("Enter your username: ")
url_events='https://api.github.com/users/'+input_username+'/events'
data=requests.get(url_events).json()
print(data)