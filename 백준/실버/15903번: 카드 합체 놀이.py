# 1. card를 최소힙으로 변환
# 2. m만큼 반복문 돌린 후 최솟값 두개 저장
# 3. 카드리스트에 최솟값 두개를 더한 값을 추가
# 4. 모든 요소 더해주기

from heapq import *

n, m = map(int, input().split())
card = list(map(int, input().split()))
# heap으로 변환
heapify(card)

for _ in range(m):
    card1 = heappop(card)
    card2 = heappop(card)
    heappush(card, card1+card2)
    heappush(card, card1+card2)

print(sum(card))