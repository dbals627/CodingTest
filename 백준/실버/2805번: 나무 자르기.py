# 144340KB 2228ms
# 1. 이분탐색을 위한 왼쪽과 오른쪽 범위 설정
# 2. 중간값을 구한 후 잘라진 나무의 총 합을 구하는 함수 호출
# 3. 총합과 나무의 길이를 비교

n, m = map(int,input().split())
h = list(map(int,input().split()))

# 잘라진 나무의 총 합을 구하는 함수
def tree(mid):
    sum = 0
    for i in h:
        if i > mid:
            sum += (i-mid)
    return sum

# 왼쪽, 오른쪽 범위 설정
lt = 0
rt = 1000000000 # 나무 최대 높이
result = 0

# 이분탐색
while lt <= rt:
    # 중간값 구하기
    mid = (lt + rt) // 2
    # 함수 호출하여 나무의 총합 계산
    total = tree(mid)

    # 총합이 나무의 길이보다 크거나 같다면
    if total >= m:
        # 결과도출
        result = mid
        # 왼쪽 범위 늘려줌
        lt = mid + 1
    # 총합이 나무의 길이보다 작다면
    # 오른쪽 범위 줄여줌
    else:
        rt = mid - 1

print(result)