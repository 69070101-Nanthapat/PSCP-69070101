"""Arcade of Time: Store Check"""
line1 = input().split()
total_stores = int(line1[0])

store_count = [0] * 1441

for _ in range(total_stores):
    time_info = input().split()
    start_time = int(time_info[0])
    stop_time = int(time_info[1])

    for minute in range(start_time, stop_time):
        store_count[minute] += 1

check_input = input().split()

answer_list = []
for item in check_input:
    target_minute = int(item)
    answer_list.append(str(store_count[target_minute]))

print(" ".join(answer_list))
