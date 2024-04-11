'''
- 스택 활용
- 같은 모양의 인형 두개가 바구니에 쌓이면 없어짐 => cnt 증가
- 같은 숫자는 같은 인형
- 2차원 배열 board, 크레인 작동 배열 moves
- moves는 세로축 인덱스, 즉 board[i][j] => j는 move-1
'''

# 인형을 뽑는 함수
def pick(board, move, stack):
    # 보드의 각 행 순회
    for i in range(len(board)):
        # 세로축 인덱스에 인형이 있다면 스택에 추가
        if board[i][move-1]:
            stack.append(board[i][move-1])
            # 인형이 이미 뽑혔으므로 0으로 바꿔줌
            board[i][move-1] = 0
            # 인형을 한개씩 뽑아서 스택에 담긴 중복된 인형 수를 판별해야 하기 때문에 break
            break

# 중복 확인 함수
def check_duplicates(stack):
    cnt = 0
    # 사라진 인형의 개수를 세기 위해서는 스택의 길이가 1보다 커야하고
    # 맨 마지막에 들어온 인형과 그 전에 들어온 인형이 같아야 한다.
    if len(stack) > 1 and stack[-1] == stack[-2]:
        # 인형 두개 제거
        stack.pop()
        stack.pop()
        # 두개씩 없어지기 때문에 +2
        cnt += 2
    return cnt

# 전체 실행 함수
def solution(board, moves):
    cnt = 0
    stack = []

    # moves 순서에 따라 인형을 뽑고 중복된 인형을 확인
    for move in moves:
        pick(board, move, stack)
        # 중복 확인 후 사라진 인형개수를 총 cnt에 더함
        cnt += check_duplicates(stack)

    return cnt