from itertools import permutations

N, M = map(int, input().split())
nums = list(map(int, input().split())) # int로 변환

result = sorted(set(permutations(nums, M)))

for i in result:
    print(' '.join(map(str, i))) # str로 변환