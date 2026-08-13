"""castle"""
n = int(input())
r = int(n ** 0.5)
if r * r < n:
    r += 1
print((r - 1) * 2)
