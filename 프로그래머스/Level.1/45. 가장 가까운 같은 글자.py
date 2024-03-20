def solution(s):
    ans = []
    dic = {}

    for i in range(len(s)):
        # 처음 나온 문자이면
        if s[i] not in dic:
            ans.append(-1)
            dic[s[i]] = i
        # 이미 나온 문자
        else:
            ans.append(i - dic[s[i]])
            # 인덱스 값 업데이트
            dic[s[i]] = i

    return ans