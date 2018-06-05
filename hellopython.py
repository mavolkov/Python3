s = input()
list = s.split()
for i in range(len(list)):
        list[i] = int(list[i])
print(sum(list))