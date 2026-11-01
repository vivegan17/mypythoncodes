import sys

def calculate_average(a, b, c):
    return (a + b + c) / 3

data = sys.stdin.read().split()

a = int(data[0])
b = int(data[1])
c = int(data[2])

result = calculate_average(a, b, c)

print(result)