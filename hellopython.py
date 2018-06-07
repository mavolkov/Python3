lst = [int(i) for i in input().split()]


def modify_list(l1):
    for i in range(len(l1)):
        if l1[i] % 2 == 0:
            l1[i] /= 2
            l1[i] = int(l1[i])
        else:
            l1[i] = -1
    while -1 in l1:
        l1.remove(-1)


modify_list(lst)
print(lst)

#изменение списка(глобальная переменная) в функции