N = int(input())
score = list(map(int, input().split()))

score_list = []
max_score = max(score)

for i in score:
    # 계산한 점수 리스트에 추가
    score_list.append((i / max_score) * 100)

# 평균 구하기
result = sum(score_list) / N
print(result)