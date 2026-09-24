studnum = int(input())
values = input().split()
for i in range(studnum) :
    n = int(values[i])
    if n >= 90:
        print("Excellent")
    elif n >= 75 and n < 90:
        print("Good")
    else:
        print("Low")
