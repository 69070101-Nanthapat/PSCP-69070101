"""shorten"""
num = []
result = []

while True:
    number = int(input())
    if number == -1:
        break
    num.append(number)

if len(num) > 0:
    start = num[0]
    end = num[0]

    for i in range(1, len(num)):
        if num[i] == end + 1:
            end = num[i]
        else:
            if start == end:
                result.append(str(start))
            else:
                result.append(f"{start}-{end}")
            start = num[i]
            end = num[i]

    if start == end:
        result.append(str(start))
    else:
        result.append(f"{start}-{end}")

    print(", ".join(result))
