import json
from urllib import request
from apiclient.discovery import build

service = build('api_name', 'api_version', ...)
best_food_chain=["chineese","dosa","idly"]
print(type(best_food_chain))
best_food_chain_dump = json.dumps(best_food_chain)
print(type(best_food_chain_dump))

# Make a dictionary
fast_food_franchise = {
    "Subway": 24722,
    "McDonalds": 14098,
    "Starbucks": 10821,
    "Pizza Hut": 7600
}

# We can also dump a dictionary to a string and load it.
fast_food_franchise_string = json.dumps(fast_food_franchise)
print(type(fast_food_franchise_string))



# Make the same request we did earlier, but with the coordinates of San Francisco instead.
parameters = {"lat": 37.78, "lon": -122.41}
response = request.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Get the response data as a python object.  Verify that it's a dictionary.
data = response.json()
print(type(data))
print(data)
