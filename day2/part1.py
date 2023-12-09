import re

id_sum = 0

colors = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def check_color(line: str, color: str):
    color_regex = r"(\d*) " + color
    matches = re.findall(color_regex, line)
    for number in matches:
        if int(number) > colors[color]:
            return False
    return True
    


with open("day2/input.txt", "r", encoding='utf8') as file:
    for line_number, line in enumerate(file, 1):
        if check_color(line, 'red') and check_color(line, 'green') and check_color(line, 'blue'):
            id_sum += line_number
    print('Sum of ids: ', id_sum)