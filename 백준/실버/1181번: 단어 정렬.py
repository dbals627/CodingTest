import sys

num = int(sys.stdin.readline())

lst = []

# 입력받은 정수 만큼 단어 출력
for i in range(num):
    # 입력한 단어 리스트에 추가
    lst.append(sys.stdin.readline().strip())
# 리스트에서 중복값 찾고(딕셔너리로 반환) 다시 리스트로 변환
lst = list(set(lst))

# 리스트를 사전순으로 정렬
lst.sort()
# 리스트를 길이로 정렬
lst.sort(key=len)

for i in lst:
    print(i)