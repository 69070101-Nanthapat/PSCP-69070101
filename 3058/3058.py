""""Brick Bridge"""
a = int(input())
b = int(input())
goal = int(input())
need_b = goal // 5
if need_b <= b:
    use_b = need_b
else:
    use_b = b
need_a = goal - (use_b * 5)
if need_a <= a:
    print(need_a)
else:
    print(-1)
