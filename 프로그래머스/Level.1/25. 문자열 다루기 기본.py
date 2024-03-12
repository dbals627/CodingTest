def solution(s):
    # str.isdigit() : 문자열이 모두 숫자로 이루어져 있는지 판별하는 함수
     return (len(s) == 4 or len(s) == 6) and s.isdigit()