import sys

data = sys.stdin.read().split()
total = float(data[0]) + float(data[1])

print(int(total) if total == int(total) else total)