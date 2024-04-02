switch_cnt = int(input())
switch = list(map(int, input().split()))
student_total = int(input())

for _ in range(student_total):
    switch_state = list(map(int, input().split()))

    # 남학생
    if switch_state[0] == 1:
        for i in range(len(switch)):
            # 3의 배수일 때
            if (i + 1) % switch_state[1] == 0:
                # 스위치 리버스
                switch[i] = 1 - switch[i]

# [0, 1, 1, 1, 0, 1, 0, 1]

    # 여학생
    if switch_state[0] == 2:
        # 3번 스위치와 좌우 대칭인 스위치 인덱스 계산
        idx = switch_state[1] - 1
        left = idx - 1
        right = idx + 1

        # 3번 스위치 리버스
        switch[idx] = 1 - switch[idx]

        # 좌우 대칭 스위치 리버스
        for _ in range(len(switch)):
            # 왼쪽 스위치는 0보다 크거나 같고
            # 오른쪽 스위치는 스위치의 개수보다 작아야 하며
            # 왼쪽과 오른쪽 스위치 상태가 같을 때
            if left >= 0 and right < switch_cnt and switch[left] == switch[right]:
                # 스위치 리버스
                switch[left] = 1 - switch[left]
                switch[right] = 1 - switch[right]
                # 스위치 범위 하나씩 늘려감
                left -= 1
                right += 1

# 출력
for i in range(switch_cnt):
    print(switch[i], end=' ')
    # 한 줄에 20개씩 출력
    if (i+1) % 20 == 0:
        print()
