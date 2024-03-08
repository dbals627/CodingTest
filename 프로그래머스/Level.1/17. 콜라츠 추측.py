# 나의 풀이
def solution(num):
    count = 0

    while num > 1 and count < 500:
        if num % 2 == 0:
            num = num // 2
        elif num % 2 == 1:
            num = num * 3 + 1
        count += 1

    return (count if num == 1 else -1)

# 팀 코드
def solution(num):
    for i in range(500):
        if num == 1:
            return i
        if (num%2==0):
            num /=2 
        else:
            num = num*3+1
    return -1