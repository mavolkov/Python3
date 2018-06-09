s = input()
result = ''

n=1
for i in range(1,len(s)):
        if s[i] == s[i-1]:
                n += 1
        else:
                result += s[i-1] + str(n)
                n = 1
result += s[len(s)-1] + str(n)
n = 1
print(result)