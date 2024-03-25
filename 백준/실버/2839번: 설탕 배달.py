import sys

n = int(sys.stdin.readline())
cnt = 0

while n >= 0:
    # 입력값이 5의 배수일 때
    if n % 5 == 0:
        cnt += n // 5
        print(cnt)
        break
    # 입력값이 5의 배수가 아닐 때
    else:
        n -= 3
        cnt += 1
# 5의 배수와 3의 배수 모두 아닐 때
else:
    print(-1)