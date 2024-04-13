'''
2579번: 계단 오르기
31120KB 52ms
'''
stair_num = int(input())
scores = [int(input()) for _ in range(stair_num)]

# 최대 점수 기록 배열
dp = [0] * (stair_num + 1)

# 첫번째 계단까지의 최대 점수는 처음 계단의 점수
dp[1] = scores[0]

# 두번째 계단까지의 최대 점수 첫번째 계단과 두번째 계단을 더한 것
if stair_num > 1:
    dp[2] = scores[0] + scores[1]

# 세번째 계단부터 마지막 계단까지 최대 점수 계산
for i in range(3, stair_num + 1):
    # 최대 점수 구하기
    # 이전 계단에서 올라온 점수 + 두 계단 전에서 올라온 점수에 현재 계단 점수를 더한 점수
    dp[i] = max(dp[i - 2], dp[i - 3] + scores[i - 2]) + scores[i - 1]

print(dp[stair_num])
