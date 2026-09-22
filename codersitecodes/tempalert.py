num = int(input())
temps = input().split()
i = 0

while i < num:
    temp = int(temps[i])
    if temp < 0:
        print("Alert")
        break
    i += 1
else:
    print("Normal")