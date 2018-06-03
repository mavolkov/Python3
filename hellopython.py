a = int(input())
while a < 8:
    a -= 1
    if a == 4:
        continue
    print(a)
    if a == 0:
        break