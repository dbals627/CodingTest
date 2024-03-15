from collections import Counter

def solution(X, Y):
    # 각 숫자의 갯수 카운터
    x = Counter(X) # {'5': 3, '2': 1}
    y = Counter(Y) # {'5': 2, '1': 1, '2': 1}

    # x와 y의 교집합 찾기
    a = x & y # ({'5': 2, '2': 1})

    result = ''

    # items() : 딕셔너리에 키-값쌍을 튜플로 반환
    for i in a.items():
        result += i[0] * i[1]

    # 짝꿍이 존재하지 않으면 -1리턴
    if len(result) == 0:
        return '-1'
    # 0번째 인덱스가 0이면 (0이 중복으로 나온다면) 0리턴
    elif result[0] == '0':
        return '0'
    # 결과를 내림차순 정렬한다음 문자열로 join
    else:
        return ''.join(sorted(result, reverse=True))