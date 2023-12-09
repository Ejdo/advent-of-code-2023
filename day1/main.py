f = open("day1/input.txt", "r")

def includes(list, item):
    for a in list:
        if a in item:
            return a
    return None

number_map = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six' : '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

final_number = 0

for line in f:

    first_number = ''
    last_number = ''

    word = ''

    for a in line:
        result = includes(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'], word)
        if result != None:
            if first_number == '':
                first_number = number_map[result]
            else:
                last_number = number_map[result]
            if word[-1] == 'e':
                word = 'e'
            elif word[-1] == 'n':
                word = 'n'
            elif word[-1] == 't':
                word = 't'
            elif word[-1] == 'o':
                word = 'o'
            else:
                word = ''
        if a in '1234567890':
            if first_number == '':
                first_number = a
                continue
            last_number = a
        else:
            word += a

    if last_number == '':
        last_number = first_number
    final_number += int(first_number + last_number)

print(final_number)