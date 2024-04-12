'''
13164번: 행복 유치원
184864KB 256ms
'''
N, K = map(int, input().split())
heights = list(map(int, input().split()))

# 키 차이 저장 리스트
diff = []
# 키 차이 계산하여 리스트에 추가
for i in range(len(heights) - 1):
    diff.append(heights[i+1] - heights[i])
# 키 차이를 오름차순 정렬
diff.sort() # 1 2 2 4

total = 0
# 최소비용 계산
for i in range(N-K):
    total += diff[i]

print(total)