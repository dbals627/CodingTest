N, K = map(int, input().split())
time = []
for _ in range(N):
    time.append(int(input()))

# 최솟값, 최댓값 범위 설정
left = min(time)
right = max(time) * K
result = float('inf')

# 이분탐색
while left <= right:
    mid = (left + right) // 2
    total = 0

    for i in time:
        total += mid // i

    if total >= K:
        right = mid - 1
        result = min(result, mid)
    else:
        left = mid + 1
print(result)