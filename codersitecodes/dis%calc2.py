import sys

discount = lambda price, percent: price * percent / 100

data = sys.stdin.read().split()
price, percent = float(data[0]), float(data[1])
print(discount(price, percent))