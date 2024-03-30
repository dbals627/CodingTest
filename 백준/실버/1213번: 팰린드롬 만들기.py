name = input()
dic = {}

# 입력 문자열과 등장 횟수를 딕셔너리에 저장
for s in name:
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1

# 반례 처리를 어떻게 해야하는지가 어려웠음
count = 0
new_dic = sorted(dic) # [A, B, C]

for s in new_dic:
    # 문자의 등장 횟수가 홀수이면 count + 1
    if dic[s] % 2 != 0:
        count += 1

        # count가 1보다 크면
        # 즉 홀수의 개수가 여러개이면 break
        if count > 1:
            print("I'm Sorry Hansoo")
            break

# 홀수 번 등장하는 문자가 1개 이하일 때
# 문자열에 추가
else:
    start = ''
    mid = ''

    # 시작 : key를 2로 나눈 값을 s번 곱하기
    # 중간 : key를 2로 나눈 나머지를 s번 곱하기
    for s in new_dic:
        start += s * (dic[s] // 2)
        mid += s * (dic[s] % 2)

    # 시작 + 중간 + 마지막(시작 리버스)
    result = start + mid + start[::-1]
    print(result)
