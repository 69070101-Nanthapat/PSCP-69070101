"""lottery"""
answer = input().split()
ans_letters = answer[0]
ans_numbers = answer[1]

lottery = input().split()
lot_letters = lottery[0]
lot_numbers = lottery[1]

prize = 0

letter_match = ans_letters == lot_letters
num_match = ans_numbers == lot_numbers
last_3_match = ans_numbers[2] == lot_numbers[2] and\
      ans_numbers[3] == lot_numbers[3] and ans_numbers[4] == lot_numbers[4]
last_2_match = ans_numbers[3] == lot_numbers[3] and ans_numbers[4] == lot_numbers[4]

if letter_match and num_match:
    prize = 1000000
elif num_match and not letter_match:
    prize = 100000
elif last_3_match and letter_match:
    prize = 2000
elif last_2_match and letter_match:
    prize = 1000
elif last_3_match and not letter_match:
    prize = 200
elif last_2_match and not letter_match:
    prize = 100
elif letter_match:
    prize = 20
else:
    prize = 0

print(prize)
