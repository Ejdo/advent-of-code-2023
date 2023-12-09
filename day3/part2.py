
def is_number(char: str):
    return char in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


def check_number(i, j, lines):
    if i < 0 or j < 0 or not is_number(lines[i][j]):
        return 0
    number = ''
    if is_number(lines[i][j]):

        if is_number(lines[i][j-1]):
            if is_number(lines[i][j-2]):
                number += lines[i][j-2]
            number += lines[i][j-1]
        number += lines[i][j]
        if is_number(lines[i][j+1]):
            number += lines[i][j+1]
            if is_number(lines[i][j+2]):
                number += lines[i][j+2]

    if number != '':
        return int(number)
    else:
        return 0


with open("day3/input.txt", "r", encoding='utf8') as file:
    lines = file.readlines()
    final_number = 0

    for line_number, line in enumerate(lines, 0):
        for row_number, row in enumerate(line, 0):
            if lines[line_number][row_number] == '*':
                part_numbers = []

                if is_number(lines[line_number-1][row_number]):
                    part_numbers.append(check_number(
                        line_number-1, row_number, lines))
                else:
                    part_numbers.append(check_number(
                        line_number-1, row_number-1, lines))
                    part_numbers.append(check_number(
                        line_number-1, row_number+1, lines))

                if is_number(lines[line_number+1][row_number]):
                    part_numbers.append(check_number(
                        line_number+1, row_number, lines))
                else:
                    part_numbers.append(check_number(
                        line_number+1, row_number-1, lines))
                    part_numbers.append(check_number(
                        line_number+1, row_number+1, lines))

                part_numbers.append(check_number(
                    line_number, row_number-1, lines))
                part_numbers.append(check_number(
                    line_number, row_number+1, lines))

                part_numbers = list(filter(lambda a: a != 0, part_numbers))

                if len(part_numbers) == 2:
                    final_number += part_numbers[0] * part_numbers[1]

    print(final_number)
