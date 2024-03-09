def solution(arr, divisor):
    num = []
    for i in arr:
        if (i % divisor == 0):
            num.append(i)

    return ([-1] if len(num) == 0 else sorted(num))

# 팀 코드
def solution(arr, divisor):
    newArr=[]
    for i in arr:
        if(i%divisor==0):
            newArr.append(i)
    if(len(newArr) == 0):
        newArr.append(-1)
    newArr.sort()
    return newArr