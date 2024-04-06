# 31120KB 44ms

# 이진 탐색으로 승률이 변하는 최솟값 구하기
# 중간값 구한 후 현재 승률을 계산
# Z보다 현재 승률이 크다면 승률을 줄이기 위해 오른쪽 범위를 줄이기
# Z보다 현재 승률이 작다면 승률을 늘리기 위해 왼쪽 범위 늘리기

X, Y = map(int, input().split())
Z = (Y * 100) // X  # (Y // X) * 100으로 하면 오류 발생

# 승률이 99% 이상일 때 더 이상 변화할 수 없음
if Z >= 99:
    print(-1)
else:
    # 범위 지정
    start = 1
    end = 1000000000 # X의 최댓값
    result = 0

    while start <= end:
        # 중간값 구하기
        mid = (start + end) // 2
        # 승률 계산하여 현재 승률보다 크다면 중간값 저장
        if (Y + mid) * 100 // (X + mid) > Z:
            result = mid
            # 오른쪽 범위 줄이기
            end = mid - 1
        else:
            # 왼쪽 범위 늘리기
            start = mid + 1
    print(result)