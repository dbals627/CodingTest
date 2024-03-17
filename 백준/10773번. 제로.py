import sys

cnt = int(sys.stdin.readline())
lst = []

for i in range(cnt):
    num = int(sys.stdin.readline())
    if num == 0:
        lst.pop()
    if num != 0:
        lst.append(num)

print(sum(lst))