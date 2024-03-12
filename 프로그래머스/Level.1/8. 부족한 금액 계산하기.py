def solution(price, money, count):
    # 총 놀이기구 이용금액 변수선언
    total = 0
    # count 범위만큼 반복문
    for i in range(1, count+1):
        # price * count
        total += price * i
    # 금액이 부족하지 않으면 0리턴
    return 0 if total - money < 0 else total - money


# 팀 코드
def solution(price, money, count):
    total = sum(price * i for i in range(1, count + 1)) 
    # 1부터 count 번 반복해서 price를 곱한 값들의 총합은 total에 담아줌
    return 0 if money - total >= 0 else total - money
    # 가진돈이 모자라지 않으면 0 그 외에는 총합에서 가진돈을 빼줌  

solution(3, 20, 4)