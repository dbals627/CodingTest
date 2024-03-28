N = int(input())

dict = {}

for _ in range(N):
    name, record = input().split()
    dict[name] = record

lst = [key for key, value in dict.items() if value == 'enter']
lst = sorted(lst, reverse=True)

for i in lst:
    print(i)