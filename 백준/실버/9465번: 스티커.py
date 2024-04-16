# 스티커
T = int(input())
for i in range(T):
    N = int(input())
    score1 = list(map(int, input().split()))
    score2 = list(map(int, input().split()))

    # dp테이블 초기화
    dp = [[0] * (N+1) for _ in range(2)]
    # 첫번째 행의 첫번째 스티커 점수 저장
    dp[0][1] = score1[0]
    # 두번째 행의 챗번째 스티커 점수 저장
    dp[1][1] = score2[0]

    # 두번째부터 마지막까지 점수 계산
    for i in range(2, N + 1):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + score1[i-1]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + score2[i-1]

    # 최댓값 출력
    print(max(dp[0][N], dp[1][N]))