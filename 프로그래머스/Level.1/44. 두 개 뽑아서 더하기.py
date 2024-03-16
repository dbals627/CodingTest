from itertools import combinations

def solution(numbers):
    comb = combinations(numbers,2)
    lst = []

    for com in comb:
        lst.append(sum(com))

    return sorted(list(set(lst)))
