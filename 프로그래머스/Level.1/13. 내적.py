def solution(a, b):
    lst = []
    for a, b in zip(a, b):
        lst.append(a * b)

    return sum(lst)