N = int(input())  # 도시의 개수
road = list(map(int, input().split()))  # 도로의 길이
cost = list(map(int, input().split()))  # 주유가격

min_cost = float('inf') # 최대 가격으로 초기화
res = 0

for dist, cost in zip(road, cost):
     # 2 5/3 2/1 4
    min_cost = min(min_cost, cost) # 최소 주유가격 갱신
    res += min_cost * dist # 최소주유가격 * 거리 = 최소비용
print(res)