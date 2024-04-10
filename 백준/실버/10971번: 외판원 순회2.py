'''
10971번: 외판원 순회2
31120KB 868ms

1. 모든 도시를 방문하는 경우의 수를 고려해 순열 사용
2. 항상 0에서 출발했다고 가정한 후 순열 조합에 따라 도시 순회
3. 경로가 없을 때 비용을 무한대로 설정한 후 break
4. 경로가 있다면 비용을 더한 후 다음 도시로 이동하기
5. 출발 도시로 돌아가는 경로도 3-4번과 같은 방식으로 적용
6. 최소비용 계속 갱신하여 출력
'''
from itertools import permutations

N = int(input())
W_arr = []
# 도시 배열 생성
for _ in range(N):
    W = list(map(int, input().split()))
    W_arr.append(W)

# 무한값 => 불가능한 경로
INF = int(1e9)
# 최소비용 초기화
min_cost = INF

# 모든 도시를 방문하는 경우의 수
for path in permutations(range(1, N)): # 1에서 N만큼의 순열 조합 생성
    cost = 0 # 비용 초기화
    start = 0 # 시작 도시 0으로 설정(고정값)

    # print(path) # (1,2,3) (1,3,2) .. (2,3,1).. (3,1,2)

    # 순열에 따라 도시 순회
    for city in path:
        # 시작도시에서 현재도시의 경로가 없을 때
        if W_arr[start][city] == 0:
            # 해당 경로로는 이동하지 못하기 때문에 무한대로 설정
            cost = INF
            break
        # 경로가 있을 때
        else:
            cost += W_arr[start][city] # 비용 누적
            start = city # 다음 도시로 이동

    # 출발 도시로 돌아가는 경로가 없을 때
    if W_arr[start][0] == 0:
        cost = INF
    # 출발 도시로 돌아가는 경로가 있을 때
    else:
        cost += W_arr[start][0] # 출발 도시로 돌아가는 비용 추가

    min_cost = min(min_cost, cost) # 최소 비용 갱신, min()을 쓰지 않으면 마지막 값만 출력되기 때문

print(min_cost)
