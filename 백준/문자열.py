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

n = int(input())
num = list(map(int, input()))
print(sum(num))

# 그대로 출력하기
while True:
    try:
        print(input())
    except EOFError:
        break
# EOFError:EOF는 END OF FILE로 사용자 입력의 끝을 나타낼 때 사용