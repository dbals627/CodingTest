n = int(input())

for i in range(1, n+1): # 1,2,3,4,5
    print(i * '*' + 2*(n-i) * ' ' + i * '*')
for j in range(n-1, 0, -1): # 4,3,2,1
    print(j * '*' + 2*(n-j) * ' ' + j * '*')
