n, m = map(int, input().split())

board = []

# 체스판
chess = ['WBWBWBWB',
           'BWBWBWBW',
           'WBWBWBWB',
           'BWBWBWBW',
           'WBWBWBWB',
           'BWBWBWBW',
           'WBWBWBWB',
           'BWBWBWBW',
           ]

# 체스판 입력
for i in range(n):
    board.append(input())

result = []

for i in range(n - 7):
    for j in range(m - 7):
        cnt = 0

        # board 에서 모든 8*8 체스판 탐색
        temp = [row[j : 8+j] for row in board[i : 8+i]]

        # 8 * 8 체스판 출력
        for k in range(8):
            for h in range(8):
              # temp와 chess를 비교
              # 각 요소들이 같지 않다면(바꿔야한다면) +1
              if temp[k][h] != chess[k][h]:
                  cnt += 1
        
        # 최솟값 구하기
        result.append(min(cnt, 64-cnt))

print(min(result))