"""giraffe"""
n = int(input())
height = []
count = 0

for i in range(n):
    h = int(input())
    height.append(h)

if n == 1:
    count = 1
else:
    for i in range(n):
        if not i:
            if height[i] > height[i + 1]:
                count += 1
        elif i == n - 1:
            if height[i] > height[i - 1]:
                count += 1
        else:
            if height[i] > height[i - 1] and height[i] > height[i + 1]:
                count += 1

print(count)
