# 문자와 문자열
word = input()
i = int(input())

print(word[i-1])

# 단어 길이 재기
word = input()
print(len(word))

# 문자열
n = int(input())

for i in range(n):
    a = str(input())
    print(a[0]+a[-1])

# 아스키 코드
a = input()
print(ord(a))

# 숫자의 합
n = input()

print(sum(map(int, input())))