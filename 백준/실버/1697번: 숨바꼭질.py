from collections import deque
n, k = map(int, input().split())
# 최대 방문 리스트
visited = [0] * 100001

def bfs():
    # 큐에 시작노드(n)를  넣어줌
    q = deque()
    q.append(n)

    # 큐가 빌때까지 반복
    while q:
        # 처음 노드를 꺼낸다
        x = q.popleft()
        # 꺼낸노드와 k가 같다면 최소 시간 출력 후 종료
        if x == k:
            print(visited[x])
            break
        # 이동 범위 정의(세방향)
        for i in (x-1, x+1, x*2):
            # 범위내에 있고 노드가 미방문이라면
            if 0 <= i <= 100000 and visited[i] == 0:
                # 노드를 방문 표시 한 후, 현재 노드까지 거리를 구함
                visited[i] = visited[x] + 1
                # 다음에 방문할 노드를 큐에 추가
                q.append(i)
bfs()