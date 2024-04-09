from heapq import *

T = int(input())

for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))
    heapify(files) # 파일 크기 리스트를 최소 힙으로 변환

    result = 0 # 결과값 저장 변수

    while len(files) > 1:
        # 최소힙에서 가장 작은 값과 그 다음 작은 값 꺼내기
        file1 = heappop(files)
        file2 = heappop(files)
        # 두개 더하기
        file_sum = file1 + file2
        # 결과에 합친 파일의 크기 더해주기
        result += file_sum
        # 합친 파일 다시 힙에 삽입
        heappush(files, file_sum)

    print(result)
