# 택배 배송
from heapq import *
INF = int(1e9)
n, m = map(int, (input().split()))

graph = [[] for i in range(n+1)] # 그래프 초기화
distance = [INF] * (n+1) # 최단 거리를 저장할 배열을 초기화

for _ in range(m):
    a,b,c = map(int, input().split())
    # 양방향 연결
    graph[a].append([b,c])
    graph[b].append([a,c])

def dijkstra(start):
    q = []
    heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heappop(q) # 최단 거리 꺼내기
        if distance[now] < dist: # 이미 처리된 노드는 무시
            continue
        for i in graph[now]:
            cost = dist + i[1] # 현재 노드를 거쳐 다른 노드로 이동하는 거리 계산
            if cost < distance[i[0]]: # 계산한 거리가 현재 저장된 거리보다 짧다면 갱신
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))
dijkstra(1)
print(distance[n])
