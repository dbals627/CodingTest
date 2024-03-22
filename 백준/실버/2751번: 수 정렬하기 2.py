import sys

num = int(sys.stdin.readline())
lst = []

for i in range(num):
    lst.append(int(sys.stdin.readline().strip()))
lst.sort()

for i in lst:
    print(i)