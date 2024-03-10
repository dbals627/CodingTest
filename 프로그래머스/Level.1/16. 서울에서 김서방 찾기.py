def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            return(f"김서방은 {i}에 있다")
        
# 팀 코드
def solution(seoul):
    return f"김서방은 {seoul.index('Kim')}에 있다"   