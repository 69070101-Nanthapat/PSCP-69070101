"""flower garden"""
thick, tar = map(int, input().split())
count = 1
floor = 0
multiplier = 1
while count <= tar:
    count += multiplier
    multiplier += 1
    floor += 1
print(__import__('math').ceil(floor / thick))
