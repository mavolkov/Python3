import requests

uni_url = 'https://stepic.org/media/attachments/course67/3.6.3/'

f = open('set.txt', 'r')
read = f.readline().strip()
lastWord = read.split('/')[-1]
f.close()

#print(lastWord)


k = 0
r = requests.get(uni_url + lastWord)

while lastWord.split('.')[-1] == 'txt':
    print(lastWord, '-', k, '-', lastWord.split('.')[-1] == 'txt')
    k += 1
    r = requests.get(uni_url + lastWord)
    lastWord = r.text.strip()



print()
print(r.text)

filename = 'result.txt'    # берем имя файла+расширение
with open(filename, 'wb') as f:  # создает и открывает файл на запись в двоичном формате
    f.write(r.content)
