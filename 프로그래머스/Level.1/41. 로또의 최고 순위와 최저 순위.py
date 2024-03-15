def solution(lottos, win_nums):
    lst = []
    result = []

    for num in win_nums:
        if num in lottos:
            lst.append(num)
            
    # 최대 순위 = 중복된 갯수 + 0의 갯수
    max_rank = len(lst) + lottos.count(0)
    # 최저 순위 = 중복된 갯수
    min_rank = len(lst)

    result.append(7 - max_rank) if max_rank >= 2 else result.append(6)
    result.append(7 - min_rank) if min_rank >= 2 else result.append(6)
    
    return result