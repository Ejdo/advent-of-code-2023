
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
        print(number)
        return int(number)
    else:
        return 0

with open("day3/input.txt", "r", encoding='utf8') as file:
    lines = file.readlines()
    final_number = 0 
                
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] in ['@', '#', '$', '%', '&', '*', '+', '/','-','=']:
                if is_number(lines[i-1][j]):
                    final_number += check_number(i-1, j, lines)
                else:
                    final_number += check_number(i-1, j-1, lines)
                    final_number += check_number(i-1, j+1, lines)
                if is_number(lines[i+1][j]):
                    final_number += check_number(i+1, j, lines)
                else:
                    final_number += check_number(i+1, j-1, lines)
                    final_number += check_number(i+1, j+1, lines)

                final_number += check_number(i, j-1, lines)
                final_number += check_number(i, j+1, lines)

                
    print(final_number)