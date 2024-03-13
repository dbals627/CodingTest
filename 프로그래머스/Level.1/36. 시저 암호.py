def solution(s, b):
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    result = ''

    for i in s:
        # 대문자
        if i.isupper():
            # 알파벳의 길이가 초과됐을 때 인덱스를 0으로 초기화
            result += upper[(upper.index(i) + b) % 26]
        # 소문자
        elif i.islower():
            result += lower[(lower.index(i) + b) % 26]
        # 공백
        else:
            result += i

    return result