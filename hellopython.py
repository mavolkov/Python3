# Quick start документация requests:
# http://docs.python-requests.org/en/master/user/quickstart/
import requests

f = open('set.txt', 'r')
url = f.readline().strip()  # читает адресную строку из файла, отрезает пробелы
f.close()

r = requests.get(url)            # открывает адрес и уже читает файл

'''
filename = url.split('/')[-1]    # берем имя файла+расширение
with open(filename, 'wb') as f:  # создает и открывает файл на запись в двоичном формате
    f.write(r.content)

k = 0  # кол-во строк
with open(filename, 'r') as f:
    for line in f:
        k += 1
print(k)
'''
with open('out.txt', 'w') as f:
    f.write(str(len(r.text.splitlines())))  # считает кол-во строк в загруженном файле
