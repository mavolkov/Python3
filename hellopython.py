f = open('set.txt', 'r')
f_out = open('out.txt', 'w')

s = ['x', 0, 0, 0]
k = 0

for line in f:
    k += 1
    sum = int(line.split(';')[1]) + int(line.split(';')[2]) + int(line.split(';')[3])
    # print(sum/3)
    f_out.write(str(sum/3) + '\n')
    s[1] += int(line.split(';')[1])
    s[2] += int(line.split(';')[2])
    s[3] += int(line.split(';')[3])
# print(s[1]/k, s[2]/k, s[3]/k)
f_out.write(str(s[1]/k)+' ' + str(s[2]/k)+' ' + str(s[3]/k)+' ')
f.close()
f_out.close()





