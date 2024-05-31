import random
import math

data = [['O', '0'], ['I', '1'], ['u', 'v']]
number_data = ['A', 'B', 'C', 'D', 'E']
level = 1
col = 3
row = 4

def start_message():
    print('Start!')

def section_message():
    print('Level: ', level)

def view_question():
    n = random.randint(0, len(data) - 1)
    q = data[n]
    print(q)
    return q

def change_input_number(input_str):
    turn_to_number = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
    letter, number = list(input_str)
    cell_number = turn_to_number[letter] + (int(number) - 1) * col
    return cell_number

def is_correct_number(mistake_number, input_number):
    return mistake_number == input_number

def view_result(is_correct):
    if is_correct:
        print('Correct!')
    else:
        print('Wrong!')

def change_string(number):
    letters = ['A', 'B', 'C', 'D', 'E']
    row = number // col + 1
    col_num = number % col
    if col_num == 0:
        col_num = col
        row -= 1
    return letters[col_num - 1] + str(row)

def play():
    global col, row

    start_message()
    section_message()
    question = view_question()

    # Dynamically display column headers
    print('/|', end="")
    for i in range(col):
        print(number_data[i], end=" ")
    print()

    # Dynamically display dashed line
    print('-' * (col * 2 + 1))

    r = 0
    while r < row:
        print(f'{r + 1}|', end="")
        c = 0
        while c < col:
            if r * col + c == random_position:
                print(question[1], end=' ')
            else:
                print(question[0], end=' ')
            c += 1
        print()
        r += 1

    input_str = 'B2'
    cell_number = change_input_number(input_str)
    print(cell_number)
    is_correct = is_correct_number(random_position, cell_number)
    view_result(is_correct)
    if not is_correct:
        correct_ans = change_string(random_position + 1)
        print(f'Correct answer is {correct_ans}')

random_position = random.randint(0, row * col - 1)

play()
