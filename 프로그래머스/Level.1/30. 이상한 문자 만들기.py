def solution(s):
    words = s.split(' ')
    new_list = []
    for i in words:
        str =''
        for j in range(len(i)):
            str+=i[j].upper() if j%2==0 else i[j].lower()
        new_list.append(str)
    return ' '.join(new_list)