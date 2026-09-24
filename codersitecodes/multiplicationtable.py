num = int(input())
for i in range(1, 51):
    prod = num * i
    if prod > 50:
        break
    print(prod)