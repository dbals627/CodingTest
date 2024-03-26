import sys

num = int(sys.stdin.readline())
people = list(map(int, sys.stdin.readline().split()))
total = 0

# 오름차순 정렬
people.sort()
# 1 2 3 3 4

for i in range(len(people)):
    total += sum(people[:i+1])

print(total)