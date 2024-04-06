from collections import Counter

N = int(input())
# 리스트에 입력값 추가
result = []
for _ in range(N):
    num = int(input())
    result.append(num)

# 산술평균
# 평균구해서 반올림
first = sum(result) / N
print(round(first))

# 중앙값
# 정렬해서 중앙 인덱스 찾음
result.sort()
print(result[len(result) // 2])

# 최빈값
# Counter 사용해서 요소의 개수 찾음
# 카운터 딕셔너리에서 최댓값을 찾아 리스트에 추가
# 최댓값이 중복되지 않는다면 0번째 요소 출력
# 중복이라면 1번째 요소 출력
third = Counter(result)
third_lst = []
for key, value in third.items():
    if value == max(third.values()):
        third_lst.append(key)
if len(third_lst) == 1:
    print(third_lst[0])
else:
    print(third_lst[1])

# 범위
# 마지막 인덱스에서 첫번째 인덱스를 빼줌
print(result[-1] - result[0])


