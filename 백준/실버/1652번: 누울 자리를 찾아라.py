N = int(input())

room_list = []
res_row = 0
res_col = 0

# 자리 리스트 생성
for _ in range(N):
    room = input()
    room_list.append(room)

for i in range(N):
    # 누울 수 있는 자리의 개수
    row = 0
    col = 0

    # 가로
    for j in range(N):
        # 자리가 있다면
        if room_list[i][j] == '.':
            row += 1
        # 자리가 없다면 0으로 초기화
        else:
            row = 0
        # 자리가 2개 있다면 결과값에 +1
        if row == 2:
            res_row += 1

    # 세로
    for j in range(N):
        # 자리가 있다면
        if room_list[j][i] == '.':
            col += 1
        # 자리가 없다면 0으로 초기화
        else:
            col = 0
        # 자리가 2개 있다면 결과값에 +1
        if col == 2:
            res_col += 1

print(res_row, res_col)


