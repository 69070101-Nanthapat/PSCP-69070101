"""pass"""
n, curr = map(int, input().split())

nxt = [0]
for _ in range(n):
    nxt.append(int(input()))

visited = [False] * (n + 1)
count = 0

while curr and not visited[curr]:
    visited[curr] = True
    count += 1
    curr = nxt[curr]

print(count)
