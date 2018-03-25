import requests

def get_planet_terrain(name):
    result = requests.get(f'http://swapi.co/api/planets?search={name}').json()
    if result['results']:
        return result['results'][0]['terrain']
    raise ValueError(f'Planet {name} not found')