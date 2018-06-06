lst = [int(i) for i in input().split()]
x = int(input())

if x in lst:
    for i in range(len(lst)):
        if x == lst[i]:
            print(i, end=' ')
else:
    print('Отсутствует')
