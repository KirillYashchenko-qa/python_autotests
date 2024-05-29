import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '782c0fc534797ad97c43d46b4c6cae96'
HEADER  = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}

body_confirmation = {'trainer_token': TOKEN}
body_create = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

body_rename = {
    "pokemon_id": "28434",
    "name": "New Name",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
print(response_rename.text)

body_catch = {"pokemon_id": "28434"}

respons_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(respons_catch.text)