N_lst = list(input().split())
lst = []

for i in N_lst:
    # 각 숫자를 리버스
    # lst에 저장
    result = i[::-1]
    lst.append(result)

# 최댓값 구하기
print(max(lst))