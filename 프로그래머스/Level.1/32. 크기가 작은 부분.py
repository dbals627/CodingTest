def solution(t, p):
    count = 0
    for i in range(len(t)):
        if t[i:i+len(p)] <= p and len(t[i:i+len(p)]) == len(p):
            count+=1
    return count
