f = open('set.txt', 'r')
f_out = open('out.txt', 'w')
a = 'ёёёёё'
d = {}
for line in f:
    l = [i.lower() for i in line.split()]
    for j in l:
        if j.isalpha():
            if j not in d.keys():
                d[j.strip()] = 1
            else:
                d[j] += 1

print(d)

for key, value in d.items():
    if value == max(d.values()):
        if key < a:
            a = key
#print('самое частое слово: ', a, max(d.values()))
#print(d)
f_out.write(a + ' ' + str(max(d.values())))
f.close()
f_out.close()





