d = {1: 'apple', 2: 'orange', 3: 'apple', 4: 'pear', 5:'orange', 6:'banana'}

# проход по ключам
for i in d:
    print(i)

# проход по ключам
for i in d.keys():
    print(i)

# проход по значениям
for i in d.values():
    print(i)

# проход по ключ-значение
for key,value in d.items():
    print(key, '-', value)