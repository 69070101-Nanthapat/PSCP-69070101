"""ab d r"""
A = int(input())
B = int(input())
d = int(input())
r = int(input())
count = 0
for x in range(A, B + 1):
    if x % d == r:
        count += 1
print(count)
