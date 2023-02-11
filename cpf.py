
import requests

cep = input(f'Informe o seu CEP: ')

api_res = requests.get(f'https://cdn.apicep.com/file/apicep/{cep}.json')

dicio = api_res.json()

for item in dicio:
    print(item, end=' - ')
    print(dicio[item])