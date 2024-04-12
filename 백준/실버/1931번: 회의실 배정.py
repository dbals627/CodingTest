'''
1931번: 회의실 배정
121900KB 408ms
'''
N = int(input())
time = []

# 회의 시작시간과 끝나는 시간 리스트에 추가
for _ in range(N):
    start, end = map(int, input().split())
    time.append((start,end))

# 끝나는 시간 기준으로 오름차순 정렬 후 시작 시간 기준으로 오름차순 정렬
time.sort(key=lambda x: (x[1], x[0]))

cnt = 0
endTime = 0

for i in time:
    # 현재 회의 시작시간이 이전 회의의 끝나는 시간보다 늦거나 같다면 +1
    # 끝나는 시간 갱신
    if i[0] >= endTime:
        endTime = i[1]
        cnt += 1
        
print(cnt)