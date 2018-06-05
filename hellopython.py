list = [int(i) for i in input().split()]
result = []
for i in list:
    if list.count(i) > 1 and i not in result:
        result.append(i)
result.sort()
for i in result:
    print(i, end=' ')
