l = []
f = open('set.tsv', 'r')
for line in f:
    l.append(line.split())


d = {}
for i in range(1, 11+1):
    d[i] = [0.0, 0]

for i in l:
    d[int(i[0])][0] += float(i[2])
    d[int(i[0])][1] += 1


for key, value in d.items():
    if value[1] != 0:
        print(key, value[0]/value[1])
    else:
        print(key, '-')