"""44 card"""
card = input().upper()
if len(card) == 2:
    if card[0] == "A":
        if card[1] == "D":
            print("ace of diamonds")
        elif card[1] == "H":
            print("ace of hearts")
        elif card[1] == "S":
            print("ace of spades")
        else:
            print("ace of clubs")

    elif card[0] == "J":
        if card[1] == "D":
            print("jack of diamonds")
        elif card[1] == "H":
            print("jack of hearts")
        elif card[1] == "S":
            print("jack of spades")
        else:
            print("jack of clubs")

    elif card[0] == "Q":
        if card[1] == "D":
            print("queen of diamonds")
        elif card[1] == "H":
            print("queen of hearts")
        elif card[1] == "S":
            print("queen of spades")
        else:
            print("queen of clubs")

    elif card[0] == "K":
        if card[1] == "D":
            print("king of diamonds")
        elif card[1] == "H":
            print("king of hearts")
        elif card[1] == "S":
            print("king of spades")
        else:
            print("king of clubs")

    elif card[0] == "2":
        if card[1] == "D":
            print("2 of diamonds")
        elif card[1] == "H":
            print("2 of hearts")
        elif card[1] == "S":
            print("2 of spades")
        else:
            print("2 of clubs")

    elif card[0] == "3":
        if card[1] == "D":
            print("3 of diamonds")
        elif card[1] == "H":
            print("3 of hearts")
        elif card[1] == "S":
            print("3 of spades")
        else:
            print("3 of clubs")

    elif card[0] == "4":
        if card[1] == "D":
            print("4 of diamonds")
        elif card[1] == "H":
            print("4 of hearts")
        elif card[1] == "S":
            print("4 of spades")
        else:
            print("4 of clubs")

    elif card[0] == "5":
        if card[1] == "D":
            print("5 of diamonds")
        elif card[1] == "H":
            print("5 of hearts")
        elif card[1] == "S":
            print("5 of spades")
        else:
            print("5 of clubs")

    elif card[0] == "6":
        if card[1] == "D":
            print("6 of diamonds")
        elif card[1] == "H":
            print("6 of hearts")
        elif card[1] == "S":
            print("6 of spades")
        else:
            print("6 of clubs")

    elif card[0] == "7":
        if card[1] == "D":
            print("7 of diamonds")
        elif card[1] == "H":
            print("7 of hearts")
        elif card[1] == "S":
            print("7 of spades")
        else:
            print("7 of clubs")

    elif card[0] == "8":
        if card[1] == "D":
            print("8 of diamonds")
        elif card[1] == "H":
            print("8 of hearts")
        elif card[1] == "S":
            print("8 of spades")
        else:
            print("8 of clubs")

    elif card[0] == "9":
        if card[1] == "D":
            print("9 of diamonds")
        elif card[1] == "H":
            print("9 of hearts")
        elif card[1] == "S":
            print("9 of spades")
        else:
            print("9 of clubs")
else:
    if card[2] == "D":
        print("10 of diamonds")
    elif card[2] == "H":
        print("10 of hearts")
    elif card[2] == "S":
        print("10 of spades")
    else:
        print("10 of clubs")
