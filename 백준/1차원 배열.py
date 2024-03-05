# 개수 세기
n = int(input())
n_list = list(map(int, input().split()))
v = int(input())

print(n_list.count(v))
# python 리스트 내장 메소드 count()는
# 매개변수로 입력된 값이 리스트 안에 몇개 있는지 세어 반환해준다.

# X보다 작은 수
N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    if A[i] < X:
        print(A[i], end = ' ')

# 최소, 최대
n = int(input())
nums = list(map(int, input().split()))

print(min(nums), max(nums))

# 최댓값
list = []
for i in range(9):
    list.append(int(input()))

print(max(list))
print(list.index(max(list))+1)

# 과제 안 내신 분..?
# 리스트 컴프리헨션 : 리스트를 생성하기 위한 간결한 방법
num = [i for i in range(1, 31)]

for _ in range(28):
    data = int(input())
    num.remove(data)
print(min(num))
print(max(num))

# 나머지
lst = []
for i in range(1, 11):
    lst.append(int(input()) % 42)

print(len(set(lst)))

