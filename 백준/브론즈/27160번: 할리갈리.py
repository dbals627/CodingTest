N = int(input())

dict = {}

for _ in range(N):
    fruit, n = input().split()

    # 딕셔너리에 key에 fruit가 없으면
    # key: fruit, value: n 값 추가
    if fruit not in dict:
        dict[fruit] = int(n)
    # 아니라면 value에 n값 계속 더하기
    else:
        dict[fruit] += int(n)

# 딕셔너리 value에 5가 있다면 YES 출력
if 5 in dict.values():
    print('YES')
else:
    print('NO')