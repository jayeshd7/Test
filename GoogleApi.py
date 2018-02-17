import urllib.request
import json
endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = 'AIzaSyABbKiwfzv9vLBR_kCuhO7w13Kseu68lr0'
origin = input('where are you ?').replace(' ','+')
destination = input('where do u want to go').replace(' ','+')
nav_request = 'origin={}&destination={}&key={}'.format(origin,destination,api_key)
request = endpoint + nav_request
response = urllib.request.urlopen(request).read().decode('utf-8')
directions = json.loads(response)
print(directions)
