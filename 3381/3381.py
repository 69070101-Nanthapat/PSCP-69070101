"""point sorting"""
t = int(input())

for _ in range(t):
    n = int(input())
    points = []

    for _ in range(n):
        x, y = map(int, input().split())
        points.append([x, y])

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i][0], points[i][1]
            x2, y2 = points[j][0], points[j][1]

            sum1 = x1 + y1
            sum2 = x2 + y2

            if sum2 < sum1 or (sum2 == sum1 and y2 > y1):
                points[i], points[j] = points[j], points[i]

    for x, y in points:
        print(x, y)
