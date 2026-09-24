num = int(input())
values = input().split()
for i in range (num):
    n = int(values[i])
    if n < 0:
        continue
    else:
        print(n)