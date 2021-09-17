import requests

r = requests.post(url='https://arnulfo190699.github.io/data/test.json', json={"nombre": "Jarx",  "edad":22})
print(r.status_code)

r = requests.get(url='https://arnulfo190699.github.io/data/test.json')
try:
    data = r.json()
    for object in data['users']:
        print(object)
except ValueError:
    print("Response content is not valid JSON")


