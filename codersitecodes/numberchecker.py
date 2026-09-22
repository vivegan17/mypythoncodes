numvalue = int(input())
values = input().split()
for i in values:
    n = int(i)
    ans = "Even" if (n % 2 == 0) else "Odd"
    print(ans)