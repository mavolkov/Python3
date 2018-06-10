import requests


url = 'https://api.coinmarketcap.com/v1/ticker/?limit=2'
r = requests.get(url)
print(r.json())