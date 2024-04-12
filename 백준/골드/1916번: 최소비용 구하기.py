'''
1916번: 최소비용 구하기
128132KB 352ms
'''
from heapq import *
INF = int(1e9)
n = int(input()) # 도시 개수
m = int(input()) # 버스 개수

graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int, input().split()) # 출발 도시, 도착 도시, 비용
    graph[a].append([b,c]) # A 도시에서 B 도시까지 가는데 드는 비용은 C

S, E = map(int, input().split()) # 출발도시, 도착도시

def dijkstra(start):
    q = [] # 최소 힙으로 최단 거리 지정
    heappush(q, (0, start)) # 시작도시와 거리를 힙에 추가
    distance[start] = 0  # 시작 도시의 거리를 0으로 설정

    while q: # 큐가 비어있지 않다면
        dist, now = heappop(q) # 최소 거리를 가진 도시를 꺼냄
        # 이미 처리된 도시라면 건너 뜀
        if distance[now] < dist:
            continue
        # 현재 도시에서 연결된 도시들 탐색
        for i in graph[now]:
            cost = dist + i[1]
            # 새로운 경로가 더 짧다면 업데이트
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))
dijkstra(S)
print(distance[E])
