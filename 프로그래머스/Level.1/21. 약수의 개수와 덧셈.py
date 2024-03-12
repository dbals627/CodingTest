def solution(left, right):
    # 결과값을 나타낼 변수를 할당
    result = 0
    # 반복문(left ~ right)
    for i in range(left, right + 1):
        # 약수의 개수를 나타낼 변수 할당
        count = 0
        # 중첩 반복문(약수 구하기, ex. j = 1에서 left)
        for j in range(1, i+1):
            # 약수이면 count 1증가
            if i % j == 0:
                count += 1
        # 출력 : 2 4 4 5 2 (각 수의 약수의 개수 출력)
        # 약수의 개수가 짝수이면 더하고 홀수이면 빼기
        if count % 2 == 0:
            result += i
        else:
            result -= i
    return result

# 팀 코드
def solution(left, right):
    total = 0 
    for i in range(left, right+1): 
        divisors = set() 
        for j in range(1, i+1): 
            if i % j == 0:
                divisors.add(j) 
                divisors.add(i // j) 
        if len(divisors) % 2 == 0: 
            total += i
        else:
            total -= i
    return total