# идентификатор объекта у каждого свой
# Получение идентификаторов (отличаются)
x = [1, 2, 3]
print(id(x))
print(id([1, 2, 3]))

# оператор is сравнивает идентификаторы
x = [1, 2, 3]
y = x
print(x is y)
print(y is x)
print(y is [1, 2, 3])

# изменяется объект, а не переменная
x = [1, 2, 3]
y = x
print(y is x)
x.append(4)
print(x)
print(y)
