import sys

def total_salary(basic, bonus):
    return basic + bonus

data = sys.stdin.read().split()
if len(data) >= 2:
    # Convert inputs to int directly if decimals aren't needed
    basic = int(data[0])
    bonus = int(data[1])
    
    print(total_salary(basic, bonus))