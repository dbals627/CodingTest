def solution(s):
    stack = []

    for i in s:
        # '('라면 리스트에 추가
        if i == '(':
            stack.append('(')
        # ')'인데 리스트가 비었다면 
        else:
            if stack == []:
                return False
            # 리스트에 '('가 있다면 지우기
            else:
                stack.pop()
    # 빈 배열이 아니라면 즉 괄호가 올바르지 않다면 False 리턴
    if stack != []:
        return False

    return True


