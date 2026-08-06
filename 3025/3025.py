"""Season"""
def main():
    """Season"""
    month = int(input())
    day = int(input())
    if day >= 21 and month in (3, 6, 9, 12):
        month += 1
    if month in (1, 2, 3):
        print("winter")
    elif month in (4, 5, 6):
        print("spring")
    elif month in (7, 8, 9):
        print("summer")
    elif month in (10, 11, 12):
        print("fall")
main()
