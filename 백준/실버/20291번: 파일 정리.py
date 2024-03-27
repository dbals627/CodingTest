# 풀이 1
N = int(input())
dict = {}

for _ in range(N):
    fileName = input().split('.')[1]
    if fileName not in dict:
        dict[fileName] = 1
    else:
        dict[fileName] += 1

sorted_dict = sorted(dict)

for i in sorted_dict:
    print(i, dict[i])

# 풀이 2

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