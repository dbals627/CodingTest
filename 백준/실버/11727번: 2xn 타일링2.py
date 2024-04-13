'''
11727번: 2xn 타일링2
31120KB 40ms
'''
n = int(input())

dp = [0] * 1001

dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
    dp[i] = dp[i-2] * 2 + dp[i-1]

print(dp[n] % 10007)