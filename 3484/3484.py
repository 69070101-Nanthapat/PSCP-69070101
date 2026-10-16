"""robot kor sound kra bueng"""
n, fine = input().split()
n = int(n)
fine = float(fine)

grid = [list(map(int, input().split())) for _ in range(n)]

col_tiles = [0] * n
col_pts = [0] * n

for row in grid:
    row_tiles = sum(1 for x in row if x > 0)
    row_pts = sum(row)

    for j in range(n):
        if row[j] > 0:
            col_tiles[j] += 1
            col_pts[j] += row[j]

    print(*row, row_tiles, row_pts)

print(*col_tiles)
print(*col_pts)

total_tiles = sum(col_tiles)
total_pts = sum(col_pts)

print(f"{total_tiles} {total_pts} {total_pts * fine:.2f}")
