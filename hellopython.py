x = int(input())
n = 0
k = 0
s = ''
while n < x:
    k += 1
    for i in range(k):
        if n == x:
            break
        print(k, end=' ')
        n += 1


