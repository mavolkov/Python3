f = open('set.txt', 'r')
f_out = open('out.txt', 'w')
a = ''
x = ''
for line in f:
    for i in range(len(line)):
        if line[i].isalpha():
            if a == '':
                a = line[i]
            else:
                print(a*int(x), end='')
                f_out.write(a*int(x))
                a = line[i]
                x = ''
        else:
            x += line[i]
    print(a*int(x))
    f_out.write(a * int(x) + '\n')
    a = ''
    x = ''

f.close()
f_out.close()
