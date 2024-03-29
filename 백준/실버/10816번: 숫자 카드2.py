from collections import Counter
# Counter는 리스트를 값으로 주게 되면
# 해당 원소들이 몇 번 등장했는지 세어 딕셔너리 형태로 반환
N = int(input())
N_Card = list(map(int, input().split()))
M = int(input())
M_Card = list(map(int, input().split()))

C_Card = Counter(N_Card)

for i in range(len(M_Card)):
    # 카드가 있다면 인덱스 찾아서 출력
    if M_Card[i] in C_Card:
        print(C_Card[M_Card[i]], end=' ')
    else:
        print(0, end=' ')