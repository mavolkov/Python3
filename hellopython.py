import requests

'''
# r = requests.get('http://example.com') # простой GET запрос
# print(r.content) # вывод ответа от сервера
# print(r.text)    # вывод ответа от сервера
'''

'''
# url = 'http://example.com'
# par = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get(url, params=par)  # Передача параметров в запрос
# print(r.url)  # Сформированный url-адрес с учетом параметров GET запроса
'''

'''
url = 'https://api.coinmarketcap.com/v1/ticker/?'
par = {'limit': '2'}  # кол-во выводимых криптовалют
r = requests.get(url, params=par)
print(r.text)
'''

'''
url = 'http://httpbin.org/cookies'
cookies = {'cookies_are': 'working'}
r = requests.get(url, cookies=cookies)  # отправка сформированных cookies на сервер
print(r.text)
print(r.cookies['example_cookie_name']) # использование cookies, полученных от сервера
'''