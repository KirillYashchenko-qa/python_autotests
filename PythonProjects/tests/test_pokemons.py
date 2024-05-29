import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '782c0fc534797ad97c43d46b4c6cae96'
HEADER  = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = 2764

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'treaner_id' : TRAINER_ID})
    assert response.status_code == 200

    def test_part_of_response():
       response_get = requests.get(url = f'{URL}/pokemons', params = {'treaner_id' : TRAINER_ID})
       assert response_get.json()['name'] == 'Кирилл147'