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
    highest_number = 0
    for number in matches:
        if int(number) > highest_number:
            highest_number = int(number)
    return highest_number
    


with open("day2/input.txt", "r", encoding='utf8') as file:
    for line in file:
        reds = check_color(line, 'red')
        greens = check_color(line, 'green')
        blues = check_color(line, 'blue')
        id_sum += reds * greens * blues
    print('Sum of ids: ', id_sum)