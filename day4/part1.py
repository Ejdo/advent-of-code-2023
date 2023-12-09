def score_scratchcard(scratch_card: str):
    winning = True
    winning_numbers = []
    correct_numbers = 0
    for row_number in range(0, len(scratch_card), 3):
        if winning:
            if scratch_card[row_number] == ' ':
                winning_numbers.append(
                    int(scratch_card[row_number+1]))
            elif scratch_card[row_number] == '|':
                winning = False
            else:
                winning_numbers.append(
                    int(scratch_card[row_number] + scratch_card[row_number+1]))
        else:
            if scratch_card[row_number] == ' ' and int(scratch_card[row_number+1]) in winning_numbers:
                correct_numbers += 1
            elif int(scratch_card[row_number] + scratch_card[row_number+1]) in winning_numbers:
                correct_numbers += 1

    if correct_numbers == 0:
        return 0
    else:
        return 2 ** (correct_numbers - 1)


with open("day4/input.txt", "r", encoding='utf8') as file:
    cards = file.readlines()
    total_points = 0

    for card in cards:
        total_points += score_scratchcard(card)

    print(total_points)
