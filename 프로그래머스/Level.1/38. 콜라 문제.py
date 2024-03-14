def solution(a, b, n):
    answer = 0
    while n >= a:
        answer += (n // a) * b #10 + 5 + 2 + 1 + 1
        n = (n % a) + (n // a) * b #10, 5, 3, 2
    return answer