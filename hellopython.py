# До ввода 'end' записывает двумерный список построчно.
# В новый список такого же размера записывает число,
# равное элементов первой матрицы на позициях
# (i-1, j), (i+1, j), (i, j-1), (i, j+1)

lst = []
double_list = []
while True:
    lst = input()
    if lst != 'end':
        double_list.append([int(i) for i in lst.split()])
    else:
        break

result = [[0 for i in range(len(double_list[0]))] for i in range(len(double_list))]


for i in range(len(result)):
    for j in range(len(result[0])):
        if -len(result)-1 <= i-1 < len(result) and -len(result)-1 <= i+1 < len(result):
            result[i][j] += double_list[i-1][j]
            result[i][j] += double_list[i+1][j]
        else:
            result[i][j] += double_list[i - 1][j]
            result[i][j] += double_list[0][j]
        if -len(result[0])-1 <= j-1 < len(result[0]) and -len(result[0])-1 <= j+1 < len(result[0]):
            result[i][j] += double_list[i][j-1]
            result[i][j] += double_list[i][j+1]
        else:
            result[i][j] += double_list[i][j - 1]
            result[i][j] += double_list[i][0]


for i in range(len(result)):
    for j in range(len(result[0])):
        print(result[i][j], end=' ')
    print()


