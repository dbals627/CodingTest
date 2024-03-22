def solution(name, yearning, photo):
    ans = []
    dic = {}

    # 딕셔너리 만들기
    for i in range(len(name)):
        dic[name[i]] = yearning[i]

    # 그리움 점수 구하기
    for photo_lst in photo:
        sum = 0
        for photo_name in photo_lst:
            if photo_name in dic:
                sum += dic[photo_name]
        ans.append(sum)

    return ans

solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]])