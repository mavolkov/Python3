d = {}
l = [i.lower() for i in input().split()]

for i in l:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] +=1

for key, value in d.items():
    print(key, value)

