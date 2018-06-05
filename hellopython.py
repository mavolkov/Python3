sum = 0
sqr = 0
while 1:
    x = int(input())
    sum += x
    sqr += x**2
    if sum == 0:
        break
print(sqr)
