# 33188KB 1004ms

# 1. 각 행을 리스트로 받는다.
# 2. 리스트의 길이만큼 반복문 => 힙의 길이가 n보다 작다면 n이 될때까지 i를 힙에 추가
# 3. 힙의 길이가 n보다 크고, i가 힙의 최솟값보다 크다면, heap에 최솟값 제거 후 i를 추가
# 4. 결국 heap에는 가장 큰 수 n개가 남을 것이고, 그 중에 최솟값을 출력한다.

from heapq import *

n = int(input())
heap = []
# n만큼 반복문
for _ in range(n):
    # 각 행을 리스트로 받음
    row = list(map(int, input().split()))
    for i in row:
        # 힙의 길이가 n보다 작다면
        # i를 힙에 추가
        if len(heap) < n:
            heappush(heap, i)
        # 힙의 길이가 n보다 크고
        else:
            # i가 최솟값보다 크다면
            # 최솟값 삭제 후 i를 추가
            if i > heap[0]:
                heappop(heap)
                heappush(heap, i)

print(heap[0])


#### 메모리 초과
# from heapq import *
#
# N = int(input())
# heap = []
#
# for _ in range(N):
#     row = list(map(int, input().split()))
#     for i in row:
#         heappush(heap, -i)
#
# result = []
# while heap:
#     result.append(-heappop(heap))
#
# # print(result)
# for i in range(len(result)):
#     if result[i] == result[N]:
#         print(result[i-1])