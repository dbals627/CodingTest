def solution(absolutes, signs):
    lst = []
    for i in range(len(signs)):
        if signs[i] == True:
            lst.append(absolutes[i])
        if signs[i] == False:
            lst.append(absolutes[i]*-1)
    return sum(lst)