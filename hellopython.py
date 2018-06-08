# f(x) определена ранее
d = {}
n = int(input())
for i in range(n):
    x = int(input())
    if x in d.keys():
        print(d[x])
    else:
        print(f(x))
        d[x] = f(x)

