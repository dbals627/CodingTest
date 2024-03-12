def solution(arr1, arr2):
    arr = []
    for arr1, arr2 in zip(arr1, arr2):
        arrs = []
        for i in range(len(arr1)):
            arrs.append(arr1[i] + arr2[i])
        arr.append(arrs)
    return arr