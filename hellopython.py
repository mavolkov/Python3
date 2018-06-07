# Принимает число n. Заполняет таблицу размером n×n,
# заполненную числами от 1 до n**2 по спирали


n = int(input())

dx, dy = 1, 0
x, y = 0, 0

lst = [[0 for i in range(n)] for j in range(n)]

for i in range(1, n ** 2 + 1):
    lst[x][y] = i
    nx, ny = x + dx, y + dy
    if 0 <= nx < n and 0 <= ny < n and not lst[nx][ny]:
        x, y = nx, ny
    else:
        dx, dy = -dy, dx
        x, y = x + dx, y + dy

for x in list(zip(*lst)):
    print(*x)


 