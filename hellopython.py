a, b, c, d = int(input()),int(input()),int(input()),int(input())

#строка 1
print('\t', end='')
for i in range(c, d+1):
    print(i,  end= '\t')
print()

#остальные строки
for i in range(a, b+1):
    print(i, end='\t')
    for j in range(c, d+1):
        print(i*j, end='\t')
    print()
