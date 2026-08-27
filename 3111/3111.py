"""SAHAKORN"""
member = input().upper()
n = int(input())
total = 0
for _ in range(n):
    buy = float(input())
    total += buy
total += 0.000000001
if member == "Y":
    total = total*0.95
    print(f"{total:.2f}")
elif member == "N" and total >= 500:
    total = total*0.97
    print(f"{total:.2f}")
else:
    print(f"{total:.2f}")
