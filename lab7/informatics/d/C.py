n = int(input())

array = list(map(int, input().split()))
temp = 0

for i in range(1, n):
    if array[i] > 0:
        temp += 1

print(temp)