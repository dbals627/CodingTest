import sys
import heapq

n, h, t = map(int, sys.stdin.readline().split())
count = 0

heap = []
for _ in range(n):
    # 최대힙을 구현하기 위해 음수로 추가
    heapq.heappush(heap, -int(sys.stdin.readline()))

for i in range(t):
    a = heapq.heappop(heap)
    # 절댓값이 h보다 작다면 조건을 만족하므로 break
    if abs(a) < h:
        heapq.heappush(heap, a)
        break
    # 키가 1이라면 값을 다시 힙에 넣어줌
    elif abs(a) == 1:
        heapq.heappush(heap,a)
    # 모두 아닐 경우 절반으로 나누어 음수처리 한 후 다시 힙에 넣어줌
    else:
        a = -(abs(a)//2)
        heapq.heappush(heap,a)
        count+=1

# 출력
if abs(min(heap)) < h:
    print('YES')
    print(count)
else:
    print('NO')
    print(abs(heapq.heappop(heap)))
