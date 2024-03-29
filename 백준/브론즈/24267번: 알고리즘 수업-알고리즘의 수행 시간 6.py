n = int(input())

sum = 0

for i in range(1, n-1): # 1~5
    sum += i * (n-2)  # 1*5 + 2*4 + 3*3 + 4*2 + 5*1
    n -= 1

print(sum)
print(3)