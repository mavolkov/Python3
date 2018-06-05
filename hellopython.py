list = [int(i) for i in input().split()]

if len(list) != 1:
    for i in range(len(list)-1):
        print(list[i-1] + list[i+1], end=' ')
    print(list[len(list)-2]+list[0])
else:
    print(list[0])

# 1 3 5 6 10



