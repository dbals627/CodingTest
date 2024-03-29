N = int(input())
user_list = set()
cnt = 0

for _ in range(N):
    word = input()

    if word != 'ENTER':
        if word not in user_list:
            cnt += 1
            user_list.add(word)
    else:
        user_list.clear()

print(cnt)