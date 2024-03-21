def solution(n, arr1, arr2):
    ans = []

    # 비트연산자 사용!!
    for i in range(n):
        num = bin(arr1[i] | arr2[i])[2:].zfill(n)
        num = num.replace('1', '#').replace('0', ' ')
        ans.append(num)
    return ans

solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])