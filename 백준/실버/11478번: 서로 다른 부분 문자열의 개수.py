import sys
str = sys.stdin.readline().strip()

lst = []

for i in range(len(str)):
    for j in range(i, len(str)):
        lst.append(str[i:j+1])

print(len(set(lst)))

