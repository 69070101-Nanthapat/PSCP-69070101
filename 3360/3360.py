"""hun kanom pang"""

d1 = input().split()
w = int(d1[0])
h = int(d1[1])

xs = [0] + [int(x) for x in input().split()] + [w]
ys = [0] + [int(y) for y in input().split()] + [h]

dx = []
i = 1
while i < len(xs):
    dx.append(xs[i] - xs[i - 1])
    i += 1

dy = []
i = 1
while i < len(ys):
    dy.append(ys[i] - ys[i - 1])
    i += 1

areas = []
for x in dx:
    for y in dy:
        areas.append(x * y)

areas.sort(reverse=True)

print(str(areas[0]) + " " + str(areas[1]))
