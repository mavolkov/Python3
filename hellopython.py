lst = [int(i) for i in input().split()]

# изменение списка c проходом с конца(глобальная переменная) в функции


def modify_list(l1):
    for i in range(len(l1)-1, -1, -1):
        if l1[i] % 2 == 0:
            l1[i] /= 2
            l1[i] = int(l1[i])
        else:
            l1.pop(i)



modify_list(lst)
print(lst)

