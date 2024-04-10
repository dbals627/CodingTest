'''
1182번: 부분수열의 합
31252KB 472ms

1. 부분수열이므로 combinations 활용
2. 정수리스트의 길이만큼 반복문을 돌려 부분수열의 길이를 늘려준다.
3. 출력된 부분수열을 리스트로 변환 후 총 합을 S와 비교
4. 총 합이 S와 같다면 cnt를 1씩 더해준다.
'''

from itertools import combinations

N,S = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0
for i in range(len(nums)):
    # 수열의 길이 늘리기
    res = combinations(nums, i+1)
    for j in res:
        # 총합이 S와 같다면 +1
        if sum(list(j)) == S:
            cnt += 1
print(cnt)

