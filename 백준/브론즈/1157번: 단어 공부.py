# 입력 받은 후 대문자로 변경
S = input().upper()

dict = {}

for i in S:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
# {'M': 1, 'I': 4, 'S': 4, 'P': 1}

cnt = list(dict.values())
# [1, 4, 4, 1]

# cnt에서 최댓값을 카운트
# 최댓값이 1개보다 많다면 물음표 출력
if cnt.count(max(cnt)) > 1:
    print('?')
    
# 최댓값을 가지고 있는 key 출력
# get : key 값이 있다면 해당 value 반환
else:
    print(max(dict, key=dict.get))