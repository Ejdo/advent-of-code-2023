def get_winning_numbers(scratch_card: str):
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

    return correct_numbers


def count_cards(cards: list):
    total_cards = 0

    for card_count in cards:
        total_cards += card_count

    return total_cards


with open("day4/input.txt", "r", encoding='utf8') as file:
    cards = file.readlines()
    total_points = 0

    cards_count = [1] * len(cards)

    for card_number, card in enumerate(cards, 0):
        number_of_copies = get_winning_numbers(card)

        for i in range(card_number, card_number + number_of_copies):
            cards_count[i+1] += cards_count[card_number]

    print(count_cards(cards_count))
