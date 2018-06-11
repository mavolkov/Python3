"""
s = []
with open('set.txt', 'r') as f:
    for i in range(4):
        s.append(f.readline().strip())
print(s)
"""

s = []
for i in range(4):
        s.append(input().strip())

coder = {}
for i in range(len(s[0])):
    coder[s[0][i]] = s[1][i]
# for key, value in coder.items():
#     print(key, '-', value)
# print()

decoder = {}
for i in range(len(s[0])):
    decoder[s[1][i]] = s[0][i]
# for key, value in decoder.items():
#     print(key, '-', value)
# print()

# coding
for i in s[2]:
    print(coder[i], end='')
print()
# decoding
for i in s[3]:
    print(decoder[i], end='')
