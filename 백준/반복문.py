# 구구단
N = int(input())

for i in range(1, 10): print(N, '*', i, '=', N*i)

# A+B
T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    print(a+b)

# 합
## for문 이용
n = int(input())

total = 0
for i in range(n+1):
    total += i
print(total)

## sum 함수 이용
print(sum(range(1, int(input()) + 1)))

# 영수증
total = int(input())
num = int(input())
prices = []

for result in range(num):
    price, n = map(int, input().split())
    prices.append(price*n)

print('Yes' if sum(prices) == total else 'No')

#코딩은 체육과목 입니다
# 반복문
for i in range(int(input())//4):
   print('long', end=' ')

print('int')

# 간단하게
print(int(input())//4*'long ' + 'int')