import json
from unittest.mock import patch

from app.swapi import get_planet_terrain


@patch('app.swapi.requests')
def test_get_planet_details(requests_mock):
    with open('tests/planet_Tatooine.json') as file:
        planets = json.load(file)

    requests_mock.get.return_value.json.return_value = planets
    assert get_planet_terrain('Tatooine') == 'desert'
    requests_mock.get.assert_called_with('http://swapi.co/api/planets?search=Tatooine')