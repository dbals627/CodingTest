a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

Fn = a1 * n0 + a0
Gn = c * n0

if Fn <= Gn and a1 <= c:
    print(1)
else:
    print(0)