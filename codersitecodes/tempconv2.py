import sys

data = sys.stdin.read().split()
celsius = float(data[0])
fahrenheit = (celsius * 9/5) + 32
print(fahrenheit)