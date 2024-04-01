max_num = 0
row = 1
col = 1

for i in range(9):
    N_list = list(map(int, input().split()))
    
    # N_list의 최댓값을 계속 갱신
    if max(N_list) > max_num:
        max_num = max(N_list) # 최댓값
        # 행 번호
        row = i + 1
        # 열 번호
        col = N_list.index(max_num) + 1

print(max_num)
print(row, col)
