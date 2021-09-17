import requests

r = requests.get(url='https://arnulfo190699.github.io/data/test.json')
try:
    data = r.json()
except ValueError:
    print("Response content is not valid JSON")