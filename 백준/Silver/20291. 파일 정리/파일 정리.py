from collections import Counter

N = int(input())
result = []
dict = {}

for _ in range(N):
    fileName = input().split('.')[1]
    result.append(fileName)

count_lst = Counter(result)

for k in sorted(count_lst):
    print(k, count_lst[k])