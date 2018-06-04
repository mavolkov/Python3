s=input()

n=0;
if s.count('g') != -1:
    n += s.count('g')
if s.count('c') != -1:
    n += s.count('c')
if s.count('G') != -1:
    n += s.count('G')
if s.count('C') != -1:
    n += s.count('C')
print(n/len(s)*100)
