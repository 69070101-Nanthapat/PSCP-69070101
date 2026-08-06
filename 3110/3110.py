"""Goods transportation"""
begin_end = input()
weight = float(input())
if begin_end == "BKK CNX":
    print(f"{10 + (30 * weight):.2f}")
elif begin_end == "CNX UBP":
    print(f"{15 + (40 * weight):.2f}")
elif begin_end == "UBP BKK":
    print(f"{20 + (40 * weight):.2f}")
elif begin_end == "BKK PKT":
    print(f"{25 + (50 * weight):.2f}")
elif begin_end == "PKT CNX":
    print(f"{30 + (60 * weight):.2f}")
elif begin_end == "UBP PKT":
    print(f"{40 + (70 * weight):.2f}")
else:
    print("Error")
