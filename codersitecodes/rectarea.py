import sys

def calculate_area(length, width=1):
    return length * width

data = sys.stdin.read().split()

length = int(data[0])
width = int(data[1]) if len(data) > 1 else 1

print(calculate_area(length, width))