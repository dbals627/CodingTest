# 해시문제

# 1. 딕셔너리로 각 카테고리의 수를 카운트 한다.
# 2. 딕셔너리 value에 값을 뽑은 후 경우의 수 계산(이 부분 검색함)
# 3. 모든 경우의 수를 계산해줘야 하기 때문에 value에 알몸인 경우를 +1
# 4. cnt에 해당값을 계속 곱해준다.
# 5. 출력시 알몸인 경우는 제외해야하기 때문에 -1

t = int(input())

for _ in range(t):
    dict = {}
    n = int(input())
    for _ in range(n):
        name, category = input().split()
        if category not in dict:
            dict[category] = 1
        else:
            dict[category] += 1
    
    # 초기값 1로 설정
    cnt = 1
    for val in dict.values():
        # 알몸일 경우 + 1
        cnt *= val + 1
    # 알몸인 경우 - 1
    print(cnt - 1)
