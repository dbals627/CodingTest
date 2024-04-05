# 144340KB 1908ms
# 1. 각 원소보다 작은수를 카운트해서 출력해아한다.
# 2. 먼저 set으로 중복을 제거한 뒤 오름차순으로 정렬해준다.
# 3. 딕셔너리를 만든 후 각 원소의 인덱스를 확인해준다.(인덱스는 각 원소보다 작은 수의 개수와 동일하기 때문)
# 4. index():시간 초과 => enumerate로 변경하여 통과

###### enumerate 사용
N = int(input())
X = list(map(int, input().split()))

sorted_X = sorted(set(X))
dict = {}
for idx, val in enumerate(sorted_X):
    dict[val] = idx
for i in X:
    print(dict[i], end=' ')

##### 시간초과
# N = int(input())
# X = list(map(int, input().split()))
#
# res = sorted(set(X))
# dict = {}
# for i in res:
#     dict[i] = res.index(i)
#
# for i in X:
#     print(dict[i], end=' ')