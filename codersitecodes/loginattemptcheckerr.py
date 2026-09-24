num = int(input())
values = input().split()  # Only 1s and 0s.
for i in range(num):
    n = int(values[i])
    if n == 1:
        print("Login Successful")
    else:
        print("Login Failed")
