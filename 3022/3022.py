"""1234"""
def main():
    """1234"""
    temp = float(input())
    temp1 = input().upper()
    temp2 = input().upper()
    if temp1 == "C":
        if temp2 == "F":
            total = temp*9/5+32
            print(f"{total:.2f}")
        elif temp2 == "K":
            total = temp + 273.15
            print(f"{total:.2f}")
        elif temp2 == "R":
            total = (temp + 273.15)*9/5
            print(f"{total:.2f}")
        elif temp2 == "C":
            print(temp)
    elif temp1 == "F":
        if temp2 == "C":
            total = (temp-32)*5/9
            print(f"{total:.2f}")
        elif temp2 == "K":
            total = (temp-32)*5/9+273.15
            print(f"{total:.2f}")
        elif temp2 == "R":
            total = temp+459.67
            print(f"{total:.2f}")
        elif temp2 == "F":
            print(temp)
    elif temp1 == "K":
        if temp2 == "F":
            total = (temp-273.15)*9/5+32
            print(f"{total:.2f}")
        elif temp2 == "C":
            total = temp-273.15
            print(f"{total:.2f}")
        elif temp2 == "R":
            total = temp*(9/5)
            print(f"{total:.2f}")
        elif temp2 == "K":
            print(temp)
    elif temp1 == "R":
        if temp2 == "F":
            total = temp - 459.67
            print(f"{total:.2f}")
        elif temp2 == "C":
            total = (temp-491.67)*5/9
            print(f"{total:.2f}")
        elif temp2 == "K":
            total = temp*(5/9)
            print(f"{total:.2f}")
        elif temp2 == "R":
            print(temp)

main()
