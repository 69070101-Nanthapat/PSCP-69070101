"""jumping frog"""
x = input().split()
step = int(x[0])
end = int(x[1])
distance = 0
jump = 0

while step > 0:
    distance += step
    jump += 1
    if distance >= end:
        break
    step -= 2

if distance >= end:
    print(jump)
else:
    print(-1)
