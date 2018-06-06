'''
def modify_list(l):
    for i in range(len(l)):
        if l[i] % 2 == 0:
            l[i] = int(l[i]/2)
        else:
            l[i] = -10
    while -10 in l:
        l.remove(-10)
    return l
'''

list = [int(i) for i in input().split()]

def modify_list():
    new_l =[]
    for i in list:
        if i % 2 == 0:
            new_l.append(int(i/2))
    list=new_l


modify_list()
print(list)
