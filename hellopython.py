# читает игры из файла
#games = []
# with open('set.txt', 'r') as f:
#    n = int(f.readline())
#    for i in range(n):
#        games.append((f.readline().strip()).split(';'))
# for i in games:
#     print(i)
# print()

# читает игры на ввод
games = []
n = int(input())
for i in range(n):
    games.append((input().strip().split(';')))

# отбираем команды
teams = {}
for i in range(n):
    if games[i][0] not in teams:
        teams[games[i][0]] = [0, 0, 0, 0, 0]
    if games[i][2] not in teams:
        teams[games[i][2]] = [0, 0, 0, 0, 0]

for i in range(n):
    if games[i][1] == games[i][3]:   # ничья
        # +1 игра
        teams[games[i][0]][0] += 1
        teams[games[i][2]][0] += 1
        # +1 ничья
        teams[games[i][0]][2] += 1
        teams[games[i][2]][2] += 1
        # +1 балл
        teams[games[i][0]][4] += 1
        teams[games[i][2]][4] += 1
    elif games[i][1] > games[i][3]:  # первая выиграла
        teams[games[i][0]][0] += 1
        teams[games[i][2]][0] += 1
        teams[games[i][0]][1] += 1
        teams[games[i][2]][3] += 1
        teams[games[i][0]][4] += 3
        teams[games[i][2]][4] += 0
    else:                            # вотрая выиграла
        teams[games[i][0]][0] += 1
        teams[games[i][2]][0] += 1
        teams[games[i][0]][3] += 1
        teams[games[i][2]][1] += 1
        teams[games[i][0]][4] += 0
        teams[games[i][2]][4] += 3

for key, value in teams.items():
    print(key + ':' + str(value[0]), value[1], value[2], value[3], value[4])
print()