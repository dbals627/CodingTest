S = input()

word = S.split('-')
result = ''

for i in word:
    result += i[0]

print(result)