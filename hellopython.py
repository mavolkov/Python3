'''
s = set()
l = []
with open('set.txt', 'r') as f:
    n = int(f.readline())
    for i in range(n):
        s.add((f.readline().strip()).lower())
    n = int(f.readline())
    for i in range(n):
        l.append((f.readline().strip()).lower())
print(s)
print(l)
'''

s = set()
l = []
n = int(input())
for i in range(n):
    s.add((input().strip()).lower())
n = int(input())
for i in range(n):
    l.append((input().strip()).lower())

user_s = set()
for i in l:
    for j in i.split():
        if j not in s:
            user_s.add(j)
for i in user_s:
    print(i)