from itertools import combinations

def solution(number):
    count = 0
    for i in list(combinations(number, 3)):
        if sum(list(i))==0:
            count+=1
            
    return count