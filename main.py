import requests

r = requests.get(url='https://arnulfo190699.github.io/data/test.json')
try:
    data = r.json()
    for object in data:
        print(object)
except ValueError:
    print("Response content is not valid JSON")


