"""Big frame"""
n1 = input()
most = len(n1)
x = []
x.append(n1)
for _ in range(4):
    nn = input()
    if len(nn) > most:
        most = len(nn)
    x.append(nn)

print("*"*(most+4))

for i in range(5):
    print(f"* {x[i]} {" "*(most-len(x[i]))}*")

print("*"*(most+4))
