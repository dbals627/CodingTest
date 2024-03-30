N,M = map(int, (input().split()))
name_dict = {}

# N과 M을 더한 길이만큼 반복문
for _ in range(N+M):
    name = input()
    if name not in name_dict:
        name_dict[name] = 1
    else:
        name_dict[name] += 1

# key 값이 2 이상일 때만 리스트에 추가
result = [key for key, value in name_dict.items() if name_dict[key] > 1]
# result의 길이 리스트에 추가 후 사전순으로 정렬
result = [len(result)] + sorted(result)

# 출력
for i in result:
    print(i)