"""score"""
n = int(input())
total = 0
for _ in range(n):
    sign = input()
    if sign == "+":
        total += 10
    elif sign == "-":
        total -= 5
print(total)
