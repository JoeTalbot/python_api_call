import os
import requests
import time

# Define function
def api_call():

    # Url variable
    url = "https://jsonplaceholder.typicode.com/todos/1"

    response = requests.request("GET", url)

    print(response.text)

# call function
api_call()
