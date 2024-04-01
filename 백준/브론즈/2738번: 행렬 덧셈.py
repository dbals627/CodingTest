N, M = map(int, (input().split()))

arr_N = [list(map(int, input().split())) for _ in range(N)]
arr_M = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        print(arr_N[i][j] + arr_M[i][j], end=' ')
    print()