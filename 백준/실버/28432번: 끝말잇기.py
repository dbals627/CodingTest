N1 = int(input())
arr_N = []

for _ in range(N1):
    word_N = input()
    arr_N.append(word_N)

M1 = int(input())
arr_M = []

for _ in range(M1):
    word_M = input()
    arr_M.append(word_M)

# print(arr_N, arr_M)
temp_word = []

for i in range(len(arr_N)):
    if N1 == 1 and M1 == 1:
        print(arr_M[0])
        break
    if arr_N[i] == '?':
        # ?가 처음 나올 때(뒷 단어만 존재)
        if i == 0:
            temp_word.append(arr_N[i+1])
            break
        # ?가 마지막으로 나올 때(앞 단어만 존재)
        if i == len(arr_N) - 1:
            temp_word.append(arr_N[i-1])
            break

        # ?가 중간에 나올 때(앞뒤단어 모두 존재)
        if i > 0 and i < len(arr_N) - 1:
            temp_word.append(arr_N[i-1])
            temp_word.append(arr_N[i+1])
            break

# 결과
for i in range(len(arr_M)):
    # ?가 처음 나올 때
    if temp_word[0][0] == arr_M[i][-1] and arr_M[i] not in arr_N:
        print(arr_M[i])
        break
    # ?가 마지막으로 나올 때
    if temp_word[0][-1] == arr_M[i][0] and arr_M[i] not in arr_N:
        print(arr_M[i])
        break
    # ?가 중간에 나올 때
    if temp_word[0][-1] == arr_M[i][0] and temp_word[1][0] == arr_M[i][-1] and arr_M[i] not in arr_N:
        print(arr_M[i])
        break


