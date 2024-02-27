# 두 수 비교하기
A, B = map(int, input().split())

if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')

## 삼항연산자
print('>') if A > B else print('<') if A < B else print('==')

# 시험 성적
score = int(input())

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')

# 윤년
# 윤년이면 1 아니면 0
# 윤년은 연도가 4의 배수, 100의 배수가 아님, 400의 배수일 때

A = int(input())

if ((A % 4 == 0) and (A % 100 != 0)) or (A % 400 == 0):
    print('1')
else:
    print('0')

# 사분면 고르기
a = int(input())
b = int(input())

if a > 0 and b > 0: print('1')
if a < 0 and b > 0: print('2')
if a < 0 and b < 0: print('3')
if a > 0 and b < 0: print('4')

# 알람 시계
H, M = map(int, input().split())

if M < 45:
    # 시간이 0시인 경우
    if H == 0:
        H = 23
        M += 60
    else:
        H -= 1
        M += 60

print(H, M-45)

# 오븐 시계
hour, min = map(int, input().split())
time = int(input())

hour += time // 60
min += time % 60

if min >= 60:
    min -= 60
    hour += 1

if hour >= 24:
    hour -= 24

print(hour, min)

# 주사위 세개
a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a * 1000)
elif a == b or b == c or a == c:
    print(1000 + a * 100) if a == c else print(1000 + b * 100)
else:
    print(max(a, b, c) * 100)





