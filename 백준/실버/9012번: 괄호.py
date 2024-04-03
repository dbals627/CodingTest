# 스택 자료구조 사용
# 문자열을 순회 후 
# 괄호쌍이 존재한다면 열린괄호를 pop
# stack이 비어있다면 YES, 아니라면 NO 프린트

N = int(input())

for i in range(N):
    stack = []
    x = input()
    for j in x:
        # '('가 있으면 stack에 추가
        if j == '(':
            stack.append('(')
        # ')'가 있으면
        else:
            # stack에 '('가 존재한다면
            # 한쌍의 괄호이므로 '('를 제거
            # 즉, 한쌍의 괄호이면 빈 배열 반환
            if '(' in stack:
                stack.pop()
            # stack에 '('가 없다면
            # 올바른 괄호쌍이 아니므로 'NO' 반환
            # break로 반복 중단
            else:
                print('NO')
                break

    # 모든 조건을 만족하고 여기까지 왔다면
    # 내부 루프가 모두 실행되고 나서 break문이 실행되지 않은 경우
    # stack이 비었다면 'YES' 아니라면 'NO'
    else:
        if stack == []:
            print('YES')
        else:
            print('NO')
            

 

