n = int(input())
marks = input().split()

for mark in marks:
    if int(mark) >= 40:
        print("Pass")
    else:
        print("Fail")