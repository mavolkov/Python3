s = input()
bykvi = []
kolvo = []

bykvi.append(s[0])
kolvo.append(1)

i=0
while s[i] == s[i+1]:
        kolvo[i] += 1
        i += 1

print(bykvi[0], end='')
print(kolvo[0], end='')
