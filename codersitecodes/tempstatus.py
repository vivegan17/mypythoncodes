tempreadings = int(input())
temperatures = input().split()
i = 0
while i < tempreadings:
    temp = int(temperatures[i])
    if temp < 20:
        print("Cold")
    elif temp >= 20 and temp <= 30:
        print("Moderate")
    else:
        print("Hot")
    i += 1