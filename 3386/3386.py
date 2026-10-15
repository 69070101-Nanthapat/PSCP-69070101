"""Duplicate ID"""
m = int(input())
n = int(input())

group1 = []
for _ in range(m):
    group1.append(input().strip())

duplicates = []
for _ in range(n):
    student_id = input().strip()
    if student_id in group1 and student_id not in duplicates:
        duplicates.append(student_id)

if not duplicates:
    print("Nope")
else:
    duplicates.sort(key=int, reverse=True)
    for student_id in duplicates:
        print(student_id)
