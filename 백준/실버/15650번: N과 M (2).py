from itertools import combinations

N, M = map(int, input().split())
lst = []

for i in range(1, N+1):
    lst.append(i)

result = combinations(lst, M)

for seq in result:
    for i in seq:
        print(i, end=' ')
    print()