s = set()
for i in range(10000000):
    s.add(i)

x = 0
for i in s:
    print(i, end='\t')
    x += 1
    if x % 20 == 0:
        print()

print()
print(555 in s)